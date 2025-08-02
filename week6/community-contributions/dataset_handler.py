import abc
import pickle

class DataSetHandler(abc.ABC):

    @abc.abstractmethod
    def load(self, target: str):
        ...
    @abc.abstractmethod
    def dump(self, dataset: list, target: str):
        ...

class PickleDataSetHandler(DataSetHandler):
    def dump(self, dataset:list, target: str):
        """Dump dataset to target pickle file."""
        print("Dumping dataset to %s", target)
        with open(target, "wb") as file:
            pickle.dump(dataset, file)
        print("Dumped dataset to %s", target)

    @classmethod
    def load(self, target: str) -> list:
        """
        Load dataset from target pickle file.

        :param target: target pickle file
        :return: dataset loaded from target pickle file
        """
        raise NotImplementedError("todo")
