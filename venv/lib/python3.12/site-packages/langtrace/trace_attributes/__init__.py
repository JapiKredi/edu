# __init__.py
from enum import Enum

from .models.database_span_attributes import DatabaseSpanAttributes
from .models.framework_span_attributes import FrameworkSpanAttributes
from .models.llm_span_attributes import LLMSpanAttributes


class SpanAttributes:
    LLM_SYSTEM = "gen_ai.system"
    LLM_OPERATION_NAME = "gen_ai.operation.name"
    LLM_REQUEST_MODEL = "gen_ai.request.model"
    LLM_REQUEST_MAX_TOKENS = "gen_ai.request.max_tokens"
    LLM_REQUEST_TEMPERATURE = "gen_ai.request.temperature"
    LLM_REQUEST_TOP_P = "gen_ai.request.top_p"
    LLM_SYSTEM_FINGERPRINT = "gen_ai.system_fingerprint"

    LLM_REQUEST_DOCUMENTS = "gen_ai.request.documents"
    LLM_REQUEST_SEARCH_REQUIRED = "gen_ai.request.is_search_required"
    LLM_PROMPTS = "gen_ai.prompt"
    LLM_CONTENT_PROMPT = "gen_ai.content.prompt"
    LLM_COMPLETIONS = "gen_ai.completion"
    LLM_CONTENT_COMPLETION = "gen_ai.content.completion"

    LLM_RESPONSE_MODEL = "gen_ai.response.model"
    LLM_USAGE_COMPLETION_TOKENS = "gen_ai.usage.output_tokens"
    LLM_USAGE_PROMPT_TOKENS = "gen_ai.usage.input_tokens"
    LLM_USAGE_TOTAL_TOKENS = "gen_ai.usage.total_tokens"
    LLM_USAGE_TOKEN_TYPE = "gen_ai.usage.token_type"
    LLM_USAGE_SEARCH_UNITS = "gen_ai.usage.search_units"
    LLM_GENERATION_ID = "gen_ai.generation_id"
    LLM_TOKEN_TYPE = "gen_ai.token.type"
    LLM_RESPONSE_ID = "gen_ai.response_id"
    LLM_URL = "url.full"
    LLM_PATH = "url.path"
    LLM_RESPONSE_FORMAT = "gen_ai.request.response_format"
    LLM_IMAGE_SIZE = "gen_ai.image.size"
    LLM_REQUEST_ENCODING_FORMATS = "gen_ai.request.encoding_formats"
    LLM_REQUEST_DIMENSIONS = "gen_ai.request.dimensions"
    LLM_REQUEST_SEED = "gen_ai.request.seed"
    LLM_REQUEST_TOP_LOGPROPS = "gen_ai.request.top_props"
    LLM_REQUEST_LOGPROPS = "gen_ai.request.log_props"
    LLM_REQUEST_LOGITBIAS = "gen_ai.request.logit_bias"

    LLM_REQUEST_TYPE = "gen_ai.request.type"
    LLM_HEADERS = "gen_ai.headers"

    LLM_USER = "gen_ai.user"
    LLM_TOOLS = "gen_ai.request.tools"
    LLM_TOOL_CHOICE = "gen_ai.request.tool_choice"
    LLM_TOOL_RESULTS = "gen_ai.request.tool_results"

    LLM_TOP_K = "gen_ai.request.top_k"
    LLM_IS_STREAMING = "gen_ai.request.stream"
    LLM_FREQUENCY_PENALTY = "gen_ai.request.frequency_penalty"
    LLM_PRESENCE_PENALTY = "gen_ai.request.presence_penalty"
    LLM_CHAT_STOP_SEQUENCES = "gen_ai.chat.stop_sequences"
    LLM_REQUEST_FUNCTIONS = "gen_ai.request.functions"
    LLM_REQUEST_REPETITION_PENALTY = "gen_ai.request.repetition_penalty"
    LLM_RESPONSE_FINISH_REASON = "gen_ai.response.finish_reasons"
    LLM_RESPONSE_STOP_REASON = "gen_ai.response.stop_reason"
    LLM_CONTENT_COMPLETION_CHUNK = "gen_ai.completion.chunk"
    # embeddings
    LLM_REQUEST_EMBEDDING_INPUTS = "gen_ai.request.embedding_inputs"
    LLM_REQUEST_EMBEDDING_DATASET_ID = "gen_ai_request_embedding_dataset_id"
    LLM_REQUEST_EMBEDDING_INPUT_TYPE = "gen_ai.request.embedding_input_type"
    LLM_REQUEST_EMBEDDING_JOB_NAME = "gen_ai.request.embedding_job_name"

    # Cohere
    LLM_COHERE_RERANK_QUERY = "gen_ai.cohere.rerank.query"
    LLM_COHERE_RERANK_RESULTS = "gen_ai.cohere.rerank.results"

    # Langtrace
    LANGTRACE_SDK_NAME = "langtrace.sdk.name"
    LANGTRACE_SERVICE_NAME = "langtrace.service.name"
    LANGTRACE_SERVICE_TYPE = "langtrace.service.type"
    LANGTRACE_SERVICE_VERSION = "langtrace.service.version"
    LANGTRACE_VERSION = "langtrace.version"

    # Http
    HTTP_MAX_RETRIES = "http.max.retries"
    HTTP_TIMEOUT = "http.timeout"


class Event(Enum):
    STREAM_START = "stream.start"
    STREAM_OUTPUT = "stream.output"
    STREAM_END = "stream.end"
    RESPONSE = "response"


class OpenAIMethods(Enum):
    CHAT_COMPLETION = "openai.chat.completions.create"
    IMAGES_GENERATION = "openai.images.generate"
    IMAGES_EDIT = "openai.images.edit"
    EMBEDDINGS_CREATE = "openai.embeddings.create"


class MistralMethods(Enum):
    CHAT_COMPLETE = "mistral.chat.complete"
    ASYNC_CHAT_COMPLETE = "mistral.chat.async_complete"
    CHAT_STREAM = "mistral.chat.stream"
    EMBEDDINGS_CREATE = "mistral.embeddings.create"
    ASYNC_EMBEDDINGS_CREATE = "mistral.embeddings.create_async"


class AWSBedrockMethods(Enum):
    CONVERSE = "aws_bedrock.converse"
    CONVERSE_STREAM = "aws_bedrock.converse_stream"


class ChromaDBMethods(Enum):
    ADD = "chromadb.collection.add"
    GET = "chromadb.collection.get"
    QUERY = "chromadb.collection.query"
    DELETE = "chromadb.collection.delete"
    PEEK = "chromadb.collection.peek"
    UPDATE = "chromadb.collection.update"
    UPSERT = "chromadb.collection.upsert"
    MODIFY = "chromadb.collection.modify"
    COUNT = "chromadb.collection.count"


class QdrantDBMethods(Enum):
    ADD = "qdrantdb.add"
    GET_COLLECTION = "qdrantdb.get_collection"
    GET_COLLECTIONS = "qdrantdb.get_collections"
    QUERY = "qdrantdb.query"
    QUERY_BATCH = "qdrantdb.query_batch"
    DELETE = "qdrantdb.delete"
    DISCOVER = "qdrantdb.discover"
    DISCOVER_BATCH = "qdrantdb.discover_batch"
    RECOMMEND = "qdrantdb.recommend"
    RECOMMEND_BATCH = "qdrantdb.recommend_batch"
    RETRIEVE = "qdrantdb.retrieve"
    SEARCH = "qdrantdb.search"
    SEARCH_BATCH = "qdrantdb.search_batch"
    UPSERT = "qdrantdb.upsert"
    COUNT = "qdrantdb.count"
    UPDATE_COLLECTION = "qdrantdb.update_collection"
    UPDATE_VECTORS = "qdrantdb.update_vectors"


class PineconeMethods(Enum):
    UPSERT = "pinecone.index.upsert"
    QUERY = "pinecone.index.query"
    DELETE = "pinecone.index.delete"


class WeaviateMethods(Enum):
    QUERY_BM25 = "weaviate.collections.queries.bm25"
    QUERY_FETCH_OBJECT_BY_ID = "weaviate.collections.queries.fetch_object_by_id"
    QUERY_FETCH_OBJECTS = "weaviate.collections.queries.fetch_objects"
    QUERY_HYBRID = "weaviate.collections.queries.hybrid"
    QUERY_NEAR_IMAGE = "weaviate.collections.queries.near_image"
    QUERY_NEAR_MEDIA = "weaviate.collections.queries.near_media"
    QUERY_NEAR_OBJECT = "weaviate.collections.queries.near_object"
    QUERY_NEAR_TEXT = "weaviate.collections.queries.near_text"
    QUERY_NEAR_VECTOR = "weaviate.collections.queries.near_vector"
    COLLECTIONS_OPERATIONS = "weaviate.collections.collections.sync"


class VendorType(Enum):
    LLM = "llm"
    VECTOR_DB = "vector_db"
    FRAMEWORK = "framework"


# Export only what you want to be accessible directly through `import my_package`
__all__ = [
    "LLMSpanAttributes",
    "SpanAttributes",
    "DatabaseSpanAttributes",
    "FrameworkSpanAttributes",
    "Event",
    "OpenAIMethods",
    "ChromaDBMethods",
    "PineconeMethods",
    "WeaviateMethods",
    "MistralMethods",
    "AWSBedrockMethods",
]
