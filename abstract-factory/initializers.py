""" Implementing AbstractFactory.

To run a AI model is needed to download two artifacts 'model' and
'configuration'. There're two ways to do so. Either via S3 or MlFlow.

The purpose is to hide a concrete initializer inside client code.
"""
from abc import ABC, abstractmethod


class InitializerFactory(ABC):
    @abstractmethod
    def initialize_model(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def initialize_configuration_files(self) -> None:
        raise NotImplementedError()


class S3Object(ABC):
    @abstractmethod
    def extract(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def download(self) -> None:
        raise NotImplementedError()


class S3Model(S3Object):
    def extract(self) -> str:
        print("\tExtracting S3 model...")

    def download(self) -> None:
        print("\tDownloading S3 model...")


class S3ConfigurationsFiles(S3Object):
    def extract(self) -> str:
        print("\tExtracting S3 configuration files...")

    def download(self) -> None:
        print("\tDownloading S3 configuration files...")


class S3Initializer(InitializerFactory):
    def initialize_model(self) -> None:
        model = S3Model()
        model.download()
        model.extract()

    def initialize_configuration_files(self) -> None:
        configuration = S3ConfigurationsFiles()
        configuration.download()
        configuration.extract()


class MlflowObject(ABC):
    @abstractmethod
    def download(self) -> None:
        raise NotImplementedError()


class MlflowModel(MlflowObject):
    def download(self) -> None:
        print("\tDownloading extracted Mlflow model...")


class MlflowConfigurationFiles(MlflowObject):
    def download(self) -> None:
        print("\tDownloading extracted Mlflow configuration files...")


class MlflowInitializer(InitializerFactory):
    def initialize_model(self) -> None:
        model = MlflowModel()
        model.download()

    def initialize_configuration_files(self) -> None:
        configuration = MlflowConfigurationFiles()
        configuration.download()


def client_code(initializer: InitializerFactory):
    """ Initialization done without knowing anything about a concrete
    initializer. """
    initializer.initialize_model()
    initializer.initialize_configuration_files()


if __name__ == "__main__":
    print("Client: Initializing via S3")
    client_code(S3Initializer())

    print("Client: Initializing via MlFlow")
    client_code(MlflowInitializer())
