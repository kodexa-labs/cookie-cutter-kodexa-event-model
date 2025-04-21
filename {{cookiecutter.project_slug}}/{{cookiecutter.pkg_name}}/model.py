"""Main module."""

from kodexa import Document, get_source, PipelineContext, KodexaClient, Assistant
from kodexa.platform.client import ProjectEndpoint, DocumentFamilyEndpoint
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def handle_event(event: BaseEvent):

    logger.info(f"Handle event called with event: {event.type}")