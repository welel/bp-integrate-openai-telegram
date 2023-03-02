from dataclasses import dataclass
import os

from dotenv import load_dotenv

from errors.errors import ImproperlyConfigured


def get_env_variable(var_name: str, cast_to=str) -> str:
    """Get an environment variable or raise an exception.

    Args:
        var_name: a name of a environment variable.
        cast_to: a type for variable casting.

    Returns:
        A value of the environment variable.

    Raises:
        ImproperlyConfigured: if the environment variable is not set.
    """
    try:
        return cast_to(os.environ[var_name])
    except KeyError:
        raise ImproperlyConfigured(var_name)
    except ValueError:
        raise ValueError("Bad environment variable casting.")


@dataclass
class Config:
    tg_token: str
    openai_token: str


def load_config() -> Config:
    # Parse a `.env` file and load the variables into environment valriables
    load_dotenv()

    return Config(
        tg_token=get_env_variable("BOT_TOKEN"),
        openai_token=get_env_variable("OPENAI_TOKEN")
    )
