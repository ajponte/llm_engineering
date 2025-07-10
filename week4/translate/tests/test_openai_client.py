import pytest

from week4.translate.clients import DEFAULT_OPENAI_MODEL
from week4.translate.clients.gpt import OpenAiApiClient, RoleName


# Pytest fixture to set up the OpenAiApiClient instance with mocks
@pytest.fixture
def client_fixture(mocker):
    """
    Fixture to set up an OpenAiApiClient instance with a mocked OpenAI client.
    The 'mocker' fixture is provided by pytest-mock and handles patching.
    """
    # Mock os.getenv to return a dummy API key for 'OPENAI_API_KEY'.
    # This is crucial because the openai library often checks this environment variable.
    # We use side_effect to return different values for different calls if needed,
    # but for a simple API key check, a direct return_value is sufficient.
    mocker.patch('os.getenv', side_effect=lambda key, default=None: 'dummy-api-key-for-test' if key == 'OPENAI_API_KEY' else default)

    # Patch the OpenAI class itself.
    # The target is 'openai.OpenAI' because that's where the class is defined,
    # and the OpenAiApiClient is expected to use this imported reference.
    mock_openai_class = mocker.patch('openai.OpenAI')

    # This is the mock instance that _client will be assigned to
    mock_openai_instance = mock_openai_class.return_value

    system_prompt = "You are a helpful assistant."
    user_prompt = "Hello, world!"
    client = OpenAiApiClient(
        system_prompt=system_prompt,
        user_prompt=user_prompt
    )
    # Return the client instance and the mock instance for assertions
    return client, mock_openai_instance, system_prompt, user_prompt

# Pytest test functions
def test_initialization(client_fixture):
    """
    Test that the OpenAiApiClient is initialized correctly.
    This test verifies:
    1. The internal _client attribute is an instance of the mocked OpenAI client.
    2. The _message_hashes list is correctly populated with system and user prompts.
    3. The _model_version is set to the default if not specified.
    """
    client, mock_openai_instance, system_prompt, user_prompt = client_fixture

    # Assert that the _client attribute is the mocked OpenAI instance
    assert client._client is mock_openai_instance

    # Assert that _message_hashes is correctly initialized
    expected_message_hashes = [
        {"role": RoleName.SYSTEM, "content": system_prompt},
        {"role": RoleName.USER, "content": user_prompt},
    ]
    assert client._message_hashes == expected_message_hashes

    # Assert that _model_version is set to the default
    assert client._model_version == DEFAULT_OPENAI_MODEL

def test_initialization_no_user_prompt(client_fixture):
    """
    Test initialization when no user prompt is provided.
    Ensures that _message_hashes handles a None user_prompt correctly.
    """
    system_prompt = "Another system prompt."
    client_no_user = OpenAiApiClient(system_prompt=system_prompt)

    expected_message_hashes = [
        {"role": RoleName.SYSTEM, "content": system_prompt},
        {"role": RoleName.USER, "content": None}, # User prompt should be None
    ]
    assert client_no_user._message_hashes == expected_message_hashes
    assert client_no_user._model_version == DEFAULT_OPENAI_MODEL

def test_initialization_custom_model_version(client_fixture):
    """
    Test initialization with a custom model version.
    Verifies that the provided model_version is correctly assigned.
    """
    custom_model = "gpt-4-turbo"
    system_prompt = "System for custom model."
    client_custom_model = OpenAiApiClient(
        system_prompt=system_prompt,
        model_version=custom_model
    )

    assert client_custom_model._model_version == custom_model
    # Ensure other attributes are still correctly set
    expected_message_hashes = [
        {"role": RoleName.SYSTEM, "content": system_prompt},
        {"role": RoleName.USER, "content": None},
    ]
    assert client_custom_model._message_hashes == expected_message_hashes
