import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        import requests
        import azure.storage.blob
        logging.info("Módulos importados correctamente.")
        return func.HttpResponse("Módulos importados correctamente.", status_code=200)
    except ImportError as e:
        logging.error(f"Error al importar módulos: {str(e)}")
        return func.HttpResponse(f"Error al importar módulos: {str(e)}", status_code=500)


        logging.info("Archivo subido con éxito al Blob Storage.")
        return func.HttpResponse("Archivo subido con éxito al Blob Storage.", status_code=200)
    except Exception as e:
        logging.error(f"Error al subir el archivo al Blob Storage: {str(e)}")
        return func.HttpResponse(f"Error al subir el archivo al Blob Storage: {str(e)}", status_code=500)