from abc import ABCMeta, abstractmethod

from src.usecases.library.dtos.create_library_request import CreateLibraryRequest
from src.usecases.library.dtos.create_library_response import CreateLibraryResponse


class CreateLibraryUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, request: CreateLibraryRequest) -> CreateLibraryResponse:
        raise NotImplementedError()