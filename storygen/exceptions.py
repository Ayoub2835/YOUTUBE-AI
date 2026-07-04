"""Custom exception hierarchy for StoryGen.

Keeping a small, explicit exception tree makes failures in the pipeline
easy to catch, log and report at the right granularity instead of leaking
raw third-party exceptions (requests.HTTPError, subprocess.CalledProcessError...)
all the way up to the CLI.
"""


class StoryGenError(Exception):
    """Base class for all StoryGen errors."""


class ConfigurationError(StoryGenError):
    """Raised when required configuration/environment variables are missing or invalid."""


class LLMGenerationError(StoryGenError):
    """Raised when story/script/metadata text generation fails."""


class TTSGenerationError(StoryGenError):
    """Raised when narration audio synthesis fails."""


class VisualGenerationError(StoryGenError):
    """Raised when scene image/video generation fails."""


class SubtitleGenerationError(StoryGenError):
    """Raised when subtitle (SRT) generation fails."""


class VideoAssemblyError(StoryGenError):
    """Raised when FFmpeg fails to assemble, mux or export a video."""


class PublishingError(StoryGenError):
    """Raised when publishing to an external platform fails."""


class ProviderNotAvailableError(StoryGenError):
    """Raised when a requested provider cannot be used (missing key/dependency)."""
