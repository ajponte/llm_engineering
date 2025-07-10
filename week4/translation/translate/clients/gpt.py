import openai

from enum import StrEnum


from translate.clients import DEFAULT_OPENAI_MODEL
from translate.error import ApiClientException


class LanguageModel(StrEnum):
    GPT = "gpt"
    CLAUDE = "claude"

class RoleName(StrEnum):
    SYSTEM = "system"
    USER = "user"

class OpenAiApiClient:
    def __init__(
        self,
        system_prompt: str,
        # todo: model version should derive from application-level config.
        model_version: str = DEFAULT_OPENAI_MODEL,
        user_prompt: str | None = None,
    ) -> None:
        """Create an OpenAI API client.

        :param system_prompt: The prompt to use for prompting for the system prompt.
                              This can be set with a later setter method.
        :param user_prompt: Optional user prompt to initialize with.
        """
        self._client = openai.OpenAI()
        # Setup a basic message hash for the model.
        self._message_hashes = [
            {"role": RoleName.SYSTEM, "content": system_prompt},
            {"role": RoleName.USER, "content": user_prompt},
        ]
        self._model_version = model_version

    def set_system_prompt(self, system_prompt: str) -> None:
        """Set the system prompt to a new value."""
        print(f"Setting SystemPrompt to {system_prompt}")
        # Update internal message hash.
        self._update_message_hash(
            role=RoleName.SYSTEM, message=system_prompt
        )

    def set_user_prompt(self, user_prompt: str) -> None:
        """Set the user prompt to a new value."""
        print(f"Setting UserPrompt to {user_prompt}")
        self._update_message_hash(
            role=RoleName.USER, message=user_prompt
        )


    def chat_stream(self):
        stream = self._execute_chat_stream()
        try:
            return self.__chunk_stream(stream)
        except Exception as ex:
            err_message = "Failed to parse GPT chat stream."
            print(err_message)
            raise ApiClientException(message=err_message, cause=ex) from ex

    def _execute_chat_stream(self):
        """Execute the chat stream via GPT client.

        :return: The result of the chat stream.
        """
        try:
            print(
                f"Executing chat stream with "
                f"model {self._model_version}, "
                f" messages: {self._message_hashes}"
            )
            stream = self._client.chat.completions.create(
                model=self._model_version,
                messages=self._message_hashes,
                stream=True
            )
            return stream
        except Exception as ex:
            err_message = f"Failed to execute GPT chat stream. Error: {ex}"
            print(err_message)
            raise ApiClientException(message=err_message, cause=ex) from ex

    def _prepare_reply(self, stream):
        return self.__chunk_stream(stream)

    def __chunk_stream(
        self,
        stream,
        initial_response:str=""
    ):
        """
        Return the stream as chunks.

        :param stream: The GPT stream to chunk.
        :param initial_response: The initial string or reply to start the chunk response.
        """
        for chunk in stream:
            fragment = chunk.choices[0].delta.content or ""
            initial_response += fragment
            print(fragment, end='', flush=True)
        return initial_response

    def _update_message_hash(
        self,
        role: RoleName,
        message: str
    ) -> None:
        """Create a new message hash for the role or update the existing one."""
        # Remove the old hash and create the new one
        self.__remove_message_hash(
            role=RoleName.USER, message_hashes=self._message_hashes
        )
        self._message_hashes.append({'role': role, 'content': message})

    @classmethod
    def __remove_message_hash(
        cls,
        role: RoleName,
        message_hashes: list[dict]
    ) -> None:
        """Remove the existing message hash for a given role."""
        # Find the index of the first dictionary that contains the key.
        # next() is used with a generator expression over enumerated items.
        # If no such dictionary is found, 'None' is returned for 'index_to_remove'.
        index_to_remove = next(
            (i for i, d in enumerate(message_hashes) if role in d),
            None
        )

        if index_to_remove is not None:
            # If a dictionary is found, create a new list by concatenating
            # the part before the found index and the part after it.
            # This avoids modifying the original list and is a functional approach.
            return message_hashes[:index_to_remove] + message_hashes[index_to_remove + 1:]
        else:
            # If no dictionary with the key is found, return a copy of the original list.
            # Returning a copy is good practice in functional programming to ensure
            # the original input is never mutated.
            return list(message_hashes)
