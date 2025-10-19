import typer
from pprint import pprint

# Import all necessary components from the generated client
from generated_client.openapi_client.api_client import ApiClient
from generated_client.openapi_client.configuration import Configuration
from generated_client.openapi_client.api.default_api import DefaultApi
from generated_client.openapi_client.exceptions import ApiException
from generated_client.openapi_client.models.document_create import DocumentCreate, DocumentType

# Create the main CLI application object
app = typer.Typer(help="A CLI client for the Document API.")

# --- Helper function for API connection ---
def get_api_instance():
    """Configures and returns an API client instance."""
    configuration = Configuration(host="http://127.0.0.1:8000")
    with ApiClient(configuration) as api_client:
        yield DefaultApi(api_client)

# --- CLI Commands ---
@app.command(name="list")
def list_all():
    """Fetches and prints all documents from the API."""
    typer.echo("Fetching all documents...")
    try:
        for api_instance in get_api_instance():
            response = api_instance.get_documents_documents_get()
            typer.echo("\n✅ Success! Found documents:")
            pprint(response)
    except ApiException as e:
        typer.echo(f"\n❌ API Error: {e.reason}", err=True)
        raise typer.Exit(code=1)

@app.command()
def list_of_owner(
        owner: str = typer.Option(..., "--owner", "-o", help="The owner of the document.")
):
    """Fetches and prints all documents from the API from a specific owner."""
    typer.echo("Fetching all documents of owner...")
    try:
        for api_instance in get_api_instance():
            response = api_instance.get_documents_documents_get(owner)
            typer.echo("\n✅ Success! Found documents:")
            pprint(response)
    except ApiException as e:
        typer.echo(f"\n❌ API Error: {e.reason}", err=True)
        raise typer.Exit(code=1)

@app.command()
def create(
        name: str = typer.Option(..., "--name", "-n", help="The name of the document."),
        owner: str = typer.Option(..., "--owner", "-o", help="The owner of the document."),
        doc_type: DocumentType = typer.Option(..., "--type", "-t", help="The document type."),
):
    """Creates a new document."""
    typer.echo(f"Creating document '{name}'...")

    doc_to_create = DocumentCreate(name=name, owner=owner, type=doc_type.value)

    try:
        for api_instance in get_api_instance():
            response = api_instance.create_document_documents_post(doc_to_create.to_dict())  # type: ignore
            typer.echo("\n✅ Successfully created document:")
            pprint(response)
    except ApiException as e:
        typer.echo(f"\n❌ API Error: {e.reason}", err=True)
        raise typer.Exit(code=1)

@app.command()
def delete(
        document_id: int = typer.Argument(..., help="The ID of the document to delete."),
):
    """Deletes a document by its ID."""
    typer.echo(f"Deleting document with ID: {document_id}...")
    try:
        for api_instance in get_api_instance():
            api_instance.delete_document_documents_document_id_delete(document_id)
            typer.echo(f"\n✅ Successfully deleted document with ID: {document_id}")
    except ApiException as e:
        typer.echo(f"\n❌ API Error: {e.reason}", err=True)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()