from dependency_injector import containers, providers
from environs import Env

from ..services.sample_service import SampleService


class Container(containers.DeclarativeContainer):
    configs = providers.Configuration()

    env = providers.Singleton(
        Env
    )

    sample_service = providers.Singleton(
        SampleService
    )
