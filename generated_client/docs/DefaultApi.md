# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_document_documents_post**](DefaultApi.md#create_document_documents_post) | **POST** /documents/ | Create Document
[**delete_document_documents_document_id_delete**](DefaultApi.md#delete_document_documents_document_id_delete) | **DELETE** /documents/{document_id} | Delete Document
[**get_document_by_id_documents_document_id_get**](DefaultApi.md#get_document_by_id_documents_document_id_get) | **GET** /documents/{document_id} | Get Document By Id
[**get_documents_documents_get**](DefaultApi.md#get_documents_documents_get) | **GET** /documents/ | Get Documents
[**update_document_documents_document_id_put**](DefaultApi.md#update_document_documents_document_id_put) | **PUT** /documents/{document_id} | Update Document


# **create_document_documents_post**
> Document create_document_documents_post(document_create)

Create Document

Creates a new document.
Example Request Body:
{
    "name": "My First Report",
    "owner": "Admin",
    "type": "PDF"
}

### Example


```python
import openapi_client
from openapi_client.models.document import Document
from openapi_client.models.document_create import DocumentCreate
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    document_create = openapi_client.DocumentCreate() # DocumentCreate | 

    try:
        # Create Document
        api_response = api_instance.create_document_documents_post(document_create)
        print("The response of DefaultApi->create_document_documents_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_document_documents_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_create** | [**DocumentCreate**](DocumentCreate.md)|  | 

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document_documents_document_id_delete**
> delete_document_documents_document_id_delete(document_id)

Delete Document

Deletes a document by its unique ID.
Example: DELETE /documents/1

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    document_id = 56 # int | 

    try:
        # Delete Document
        api_instance.delete_document_documents_document_id_delete(document_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_document_documents_document_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_by_id_documents_document_id_get**
> Document get_document_by_id_documents_document_id_get(document_id)

Get Document By Id

Retrieves a single document by its unique ID.
Example: /documents/1

### Example


```python
import openapi_client
from openapi_client.models.document import Document
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    document_id = 56 # int | 

    try:
        # Get Document By Id
        api_response = api_instance.get_document_by_id_documents_document_id_get(document_id)
        print("The response of DefaultApi->get_document_by_id_documents_document_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_document_by_id_documents_document_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **int**|  | 

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_documents_documents_get**
> List[Document] get_documents_documents_get(owner=owner)

Get Documents

Gets a list of all documents.
Can optionally be filtered by the 'owner' query parameter.
Example: /documents/?owner=Admin

### Example


```python
import openapi_client
from openapi_client.models.document import Document
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    owner = 'owner_example' # str |  (optional)

    try:
        # Get Documents
        api_response = api_instance.get_documents_documents_get(owner=owner)
        print("The response of DefaultApi->get_documents_documents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_documents_documents_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | [optional] 

### Return type

[**List[Document]**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_document_documents_document_id_put**
> Document update_document_documents_document_id_put(document_id, document_create)

Update Document

Updates an existing document by its unique ID.
Example: PUT /documents/1
With Request Body:
{
    "name": "My Updated Report",
    "owner": "Admin",
    "type": "Word Doc"
}

### Example


```python
import openapi_client
from openapi_client.models.document import Document
from openapi_client.models.document_create import DocumentCreate
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    document_id = 56 # int | 
    document_create = openapi_client.DocumentCreate() # DocumentCreate | 

    try:
        # Update Document
        api_response = api_instance.update_document_documents_document_id_put(document_id, document_create)
        print("The response of DefaultApi->update_document_documents_document_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_document_documents_document_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **int**|  | 
 **document_create** | [**DocumentCreate**](DocumentCreate.md)|  | 

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

