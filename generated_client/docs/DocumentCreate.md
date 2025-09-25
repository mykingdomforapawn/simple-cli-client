# DocumentCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**owner** | **str** |  | 
**type** | [**DocumentType**](DocumentType.md) |  | 

## Example

```python
from openapi_client.models.document_create import DocumentCreate

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCreate from a JSON string
document_create_instance = DocumentCreate.from_json(json)
# print the JSON string representation of the object
print(DocumentCreate.to_json())

# convert the object into a dict
document_create_dict = document_create_instance.to_dict()
# create an instance of DocumentCreate from a dict
document_create_from_dict = DocumentCreate.from_dict(document_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


