[![Build Status](https://travis-ci.org/EvidentSecurity/esp-sdk-python2.svg?branch=master)](https://travis-ci.org/EvidentSecurity/esp-sdk-python2)
[![Gem Version](https://badge.fury.io/py/esp-sdk-python2.svg)](http://badge.fury.io/py/esp-sdk-python2)

# This SDK is still a work in progress.  Once it is ready for Beta testing, a beta release will be published to PyPi.

# esp_sdk
The Evident Security Platform API (version 2.0) is designed to allow users granular control over their Amazon Web Service security experience by allowing them to review alerts, monitor signatures, and create custom signatures.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v2_sdk
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

```sh
pip install esp_sdk
```

Or you can install directly from Github

```sh
pip install git+https://github.com/EvidentSecurity/esp-sdk-python2.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/EvidentSecurity/esp-sdk-python2.git`)

Then import the package:
```python
import esp_sdk 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import esp_sdk
```

## Set your HMAC security keys:

You must set your access_key_id and your secret_access_key.
You can set these directly:

```python
config = esp_sdk.Configuration()
config.access_key_id = '<your key>'
config.secret_access_key = '<your secret key>'
```

or with environment variables:

```python
os.environ['ESP_ACCESS_KEY_ID'] = '<your key>'
os.environ['ESP_SECRET_ACCESS_KEY'] = '<your secret key>'
```

Get your HMAC keys from the Evident.io website, [esp.evident.io](https://esp.evident.io/settings/api_keys)

## Appliance Users

Users of Evident.io's AWS marketplace PSAAS/appliance will need to set the host for their appliance instance.
You can set this directly:

```python
config = esp_sdk.Configuration().host = '<host for appliance instance>'
```
The host needs to include the scheme. Example:  `config.host = 'https://api.evident.io'` This is the default.

Alternatively, the site can also be set with an environment variable.

```
export ESP_HOST=<host for appliance instance>
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

    
# create an instance of the API class
api_instance = esp_sdk.AlertsApi()
report_id = 56 # int | Id of the Report to Return Alerts For
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attribute: [id]  Limited Searchable Attributes: [signature_service_id_in, signature_risk_level_in, risk_level_in, risk_level_eq, resource_or_tag_cont, suppressed, not_suppressed, signature_name_cont, signature_identifier_cont, external_account_id_in, external_account_id_eq, external_account_team_id_in, external_account_team_id_eq, region_id_in, region_id_eq, status_in, status_eq, cloud_trail_events_present, open_as_of, signature_id_in, signature_id_eq]   Example: filter: {name_eq: 'Bob'} (optional)
include = 'include_example' # str | Objects that can be included in the response:  external_account,region,signature,custom_signature,suppression,metadata,cloud_trail_events,tags,compliance_controls  See Including Objects for more information. (optional)
page = {'key': 'page_example'} # dict(str, str) | Page Number and Page Size.  Example: page: {number: 1, size: 20} (optional)

try:
    # Get a list of Alerts
    api_response = api_instance.list(report_id, filter=filter, include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->list: %s\n" % e)


```
## Errors
The response objects have an errors collection.  If the API call returns a non fatal response, like
validation issues, you can check the errors object to see what went wrong.

```python
> t = esp_sdk.TeamsApi().create(1, '')
# => t.errors = ["Name can't be blank"]
```

When an error is thrown, you can rescue the error and check the error message:

```python
> c = esp_sdk.SignaturesApi().run(1, 9999, 'us-east-1')
# =>  esp_sdk.rest.ApiException: (404)
# =>  Reason: Failed.  Response code = 404.  Response message = Couldn't find ExternalAccount
```

## Pagination
Evident.io API endpoints that return a collection of objects allows for paging and only returns a limited number of items at a time.
The Evident.io SDK returns an esp_sdk.PaginatedCollection object that provides methods for paginating through the collection.

```python
> alerts = esp_sdk.AlertsApi().list(345)
> alerts.current_page_number # => "1"
> page2 = alerts.next_page()
> alerts.current_page_number # => "1"
> page2.current_page_number # => "2"
> page1 = page2.previous_page()
> page1.current_page_number # => "1"
> last_page = alerts.last_page()
> last_page.current_page_number # => "25"
> page4 = alerts.page(4)
> page4.current_page_number # => "4"
```

The `__iter__` function on esp_sdk.PaginatedCollection allows you to iterate through the entire
collection, making additional API calls to get the next page, until it is on the last page.

```python
> alerts = esp_sdk.AlertsApi().list(345)
> [a.id for a in alerts]
```

See esp_sdk.PaginatedCollection for all the pagination methods available.

## Including Objects
Most of the objects in the Evident.io SDK have a corresponding API call associated with it.  That means if you want an object's
associated object, then you will make another API call using the associated objects api.  For example:

```python
> external_account = esp_sdk.ExternalAccountsApi().show(3)
> organization = esp_sdk.OrganizationsApi().show(external_account.organization_id)
> sub_organization = esp_sdk.SubOrganizationsApi().show(external_account.sub_organization_id)
> team = esp_sdk.TeamsApi().show(external_account.team_id)
```

The above code will make 4 calls to the Evident.io API.  1 each for the external account, organization, sub_organization and team.
The [JSON API Specification](http://jsonapi.org/format/#fetching-includes), which the Evident.io API tries to follow, provides
a means for returning nested objects in a single call.  With the SDK, that can be done by providing a comma separated string
of the relations wanted in an +include+ option.

```python
> external_account = esp_sdk.ExternalAccountsApi().show(3, include='organization,sub_orgnanization,team')
```

```python
> external_account = esp_sdk::ExternalAccountsApi().list(id_eq: 3, include='organization,sub_organization,team')
```

With that call, organization, sub_organization and team will all come back in the response, and calling, `external_account.organization`,
`external_account.sub_organization` and `external_account.team` will return the associated object.

You can nest include requests with the dot property. For example, requesting `external_account.team` on an alert will expand the `external_account` property into a full `External Account` object, and will then expand the `team` property on that external account into a full `Team` object.
Deep nesting is available as well.  `external_account.team.organization`

```python
alert = esp_sdk.AlertsApi().show(1, include='tags,external_account.team')

alerts = esp_sdk.AlertsApi().list(4, include='tags,external_account.team')
```

Most objects' show and list methods accept the +include+ option.  Those methods that accept the +include+ option are documented with the available associations that are includable.

## Filtering/Searching
For objects that implement `list`, parameters can be passed that will filter the results based on the search criteria specified.
The criteria that can be specified depends on the object.  Each object is documented whether it implements `list` or not,
and if so, which attributes can be included in the search criteria.

### Searching

The primary method of searching is by using what is known as *predicates*.

Predicates are used within Evident.io API search queries to determine what information to
match. For instance, the `cont` predicate, when added to the `name` attribute, will check to see if `name`` contains a value using a wildcard query.

```python
esp_sdk.SignaturesApi().list(filter={ "name_cont": 'dns' })
#=> will return signatures `where name LIKE '%dns%'`
```

### Conditions on Relationships

The syntax for queries on an associated relationship is to just append the association name to the attribute:

```python
esp_sdk.SuppressionsApi().list(filter={ "regions_code_eq": 'us_east_1' })
#=> will return suppressions that have a region relationship `where code = 'us_east_1'`
```

### Complex Filtering

Add multiple attributes and predicates to form complex queries:

```python
esp_sdk.SuppressionsApi().list(filter={ "regions_code_start": 'us', "created_by_email_eq": 'bob@mycompany.com', resource_not_null: '1' })
#=> will return suppressions that have a region relationship `where code LIKE 'us%'` and created_by relationship `where email = 'bob@mycompany.com'` and `resource IS NOT NULL`
```

You can also change the `combinator` for complex queries from the default `AND` to `OR` by adding the `m: 'or'` parameter

```python
esp_sdk.SuppressionsApi().list(filter={ "regions_code_start": 'us', "created_by_email_eq": 'bob@mycompany.com', resource_not_null: '1', m: 'or' })
#=> will return suppressions that have a region relationship `where code LIKE 'us%'` **OR** created_by relationship `where email = 'bob@mycompany.com'` **OR** `resource IS NOT NULL`
```

### Bad Attributes

**Please note:** any attempt to use a predicate for an attribute that does not exist will return a
*422 (Unprocessable Entity)* response. For instance, this will not work:

```python
esp_sdk.SuppressionsApi().list(filter={ "bad_attribute_eq": 'something' })
#=> esp_sdk.ApiError()iled.  Response code = 422.  Response message = Invalid search term bad_attribute_eq.
```

**Also note:** any attempt to use a predicate for an attribute that exists on the object, but is not a documented searchable attribute will _silently fail_
and will be excluded from the search criteria.

## Available Predicates

Below is a list of the available predicates and their opposites.

### eq (equals)

The `eq` predicate returns all records where a field is *exactly* equal to a given value:

```python
esp_sdk.SuppressionsApi().list(filter={ "regions_code_eq": 'us_east_1' })
#=> will return suppressions that have a region relationship `where code = 'us_east_1'`
```

**Opposite: `not_eq`**

### lt (less than)

The `lt` predicate returns all records where a field is less than a given value:

```python
from datetime import datetime, timedelta
esp_sdk.ReportsApi().list(filter={ "created_at_lt": datetime.now() - timedelta(hours = 1) })
#=> will return reports `where created_at < '2015-11-11 16:25:30'`
```

**Opposite: `gt` (greater than)**

### lteq (less than or equal to)

The `lteq` predicate returns all records where a field is less than *or equal to* a given value:

```python
from datetime import datetime, timedelta
esp_sdk.ReportsApi().list(filter={ "created_at_lteq": datetime.now() - timedelta(hours = 1) })
#=> will return reports `where created_at <= '2015-11-11 16:25:30'`
```

**Opposite: `gteq` (greater than or equal to)**

### in

The `in` predicate returns all records where a field is within a specified list:

```python
esp_sdk.SignaturesApi().list(filter={ "risk_level_in": ['Low', 'Medium'] })
#=> will return signatures `where risk_level IN ('Low', 'Medium')`
```

**Opposite: `not_in`**

### cont (contains)

The `cont` predicate returns all records where a field contains a given value:

```python
esp_sdk.SignaturesApi().list(filter={ "name_cont": 'dns' })
#=> will return signatures `where name LIKE '%dns%'`
```

**Opposite: `not_cont`**

**Please note:** This predicate is only available on attributes listed in the "Valid Matching Searchable Attributes"" section
for each implemented `where` method.

### cont_any (contains any)

The `cont_any` predicate returns all records where a field contains any of given values:

```python
esp_sdk.SignaturesApi().list(filter={ "name_cont_any": ['dns', 'EC2'] })
#=> will return signatures `where name LIKE '%dns%' or name LIKE '%EC2%'`
```

**Opposite: `not_cont_any`**

**Please note:** This predicate is only available on attributes listed in the "Valid Matching Searchable Attributes"" section
for each implemented `where` method.


### start (starts with)

The `start` predicate returns all records where a field begins with a given value:

```python
esp_sdk.SignaturesApi().list(filter={ "name_start": 'dns' })
#=> will return signatures `where name LIKE 'dns%'`
```

**Opposite: `not_start`**

**Please note:** This predicate is only available on attributes listed in the "Valid Matching Searchable Attributes"" section
for each implemented `where` method.

### end (ends with)

The `end` predicate returns all records where a field ends with a given value:

```python
esp_sdk.SignaturesApi().list(filter={ "name_end": 'dns' })
#=> will return signatures `where name LIKE '%dns'`
```

**Opposite: `not_end`**

**Please note:** This predicate is only available on attributes listed in the "Valid Matching Searchable Attributes"" section
for each implemented `where` method.

### present

The `present` predicate returns all records where a field is present (not null and not a
blank string).

```python
esp_sdk.SignaturesApi().list(filter={ "identifier_present": '1' })
#=> will return signatures `where identifier IS NOT NULL AND identifier != ''`
```

**Opposite: `blank`**

### null

The `null` predicate returns all records where a field is null:

```python
esp_sdk.SignaturesApi().list(filter={ "identifier_null": 1 })
#=> will return signatures `where identifier IS NULL`
```

**Opposite: `not_null`**

## Sorting

Lists can also be sorted by adding the `sorts` parameter with the field to sort by to the `filter` parameter.

```python
esp_sdk.SignaturesApi().list(filter={ "name_cont": 'dns', "sorts": 'risk_level desc' })
#=> will return signatures `where name LIKE '%dns%'` sorted by `risk_level` in descending order.
```

Lists can be sorted by multiple fields by specifying an ordered array.

```python
esp_sdk.SignaturesApi().list(filter={ "name_cont": 'dns', "sorts": ['risk_level desc', 'created_at'] })
#=> will return signatures `where name LIKE '%dns%'` sorted by `risk_level` in descending order and then by `created_at` in ascending order.
    ```    
    
## Documentation for API Endpoints

All URIs are relative to *https://api.evident.io/*

### Searchable Attributes on List Endpoints

The description of the filter parameter for the list endpoints have the searchable attributes separated into different lists.

#### Equality Searchable Attributes

These attributes can be used with predicates that look for an exact match such as **eq**

#### Matching Searchable Attribute

These attributes can be used with predicates that look for a string that matches the supplied string such as **cont**

#### Limited Searchable Attributes

These attributes cannot be used with every predicate.  Only with the predicates listed.

#### Searchable Associations

These are associations you can search through.  See the documentation for each association to see which attributes are searchable.

#### Sortable Attributes

These attributes can be passed with the **sorts** key to sort the response.

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AlertsApi* | [**list**](docs/AlertsApi.md#list) | **PUT** /api/v2/reports/{report_id}/alerts.json_api | Get a list of Alerts
*AlertsApi* | [**show**](docs/AlertsApi.md#show) | **GET** /api/v2/alerts/{id}.json_api | Show a single Alert
*AuditLogFileExportApi* | [**create**](docs/AuditLogFileExportApi.md#create) | **POST** /api/v2/audit_logs/export/files.json_api | Export an Audit Log File
*AuditLogFileExportApi* | [**show**](docs/AuditLogFileExportApi.md#show) | **GET** /api/v2/audit_logs/export/files/{id}.json_api | Show a single Audit Log File
*AuditLogsApi* | [**list**](docs/AuditLogsApi.md#list) | **PUT** /api/v2/audit_logs.json_api | Get a list of Audit Logs
*AuditLogsApi* | [**show**](docs/AuditLogsApi.md#show) | **GET** /api/v2/audit_logs/{id}.json_api | Show a single Audit Log
*CloudTrailEventsApi* | [**list**](docs/CloudTrailEventsApi.md#list) | **GET** /api/v2/alerts/{alert_id}/cloud_trail_events.json_api | Get a list of Cloud Trail Events
*CloudTrailEventsApi* | [**show**](docs/CloudTrailEventsApi.md#show) | **GET** /api/v2/cloud_trail_events/{id}.json_api | Show a single Cloud Trail Event
*ComplianceControlsApi* | [**list**](docs/ComplianceControlsApi.md#list) | **PUT** /api/v2/compliance_controls.json_api | Get a list of Compliance Controls
*ComplianceControlsApi* | [**show**](docs/ComplianceControlsApi.md#show) | **GET** /api/v2/compliance_controls/{id}.json_api | Show a single Compliance Control
*ComplianceDomainsApi* | [**list**](docs/ComplianceDomainsApi.md#list) | **PUT** /api/v2/compliance_domains.json_api | Get a list of Compliance Domains
*ComplianceDomainsApi* | [**show**](docs/ComplianceDomainsApi.md#show) | **GET** /api/v2/compliance_domains/{id}.json_api | Show a single Compliance Domain
*ComplianceStandardsApi* | [**list**](docs/ComplianceStandardsApi.md#list) | **PUT** /api/v2/compliance_standards.json_api | Get a list of Compliance Standards
*ComplianceStandardsApi* | [**show**](docs/ComplianceStandardsApi.md#show) | **GET** /api/v2/compliance_standards/{id}.json_api | Show a single Compliance Standard
*ContactRequestsApi* | [**create**](docs/ContactRequestsApi.md#create) | **POST** /api/v2/contact_requests.json_api | Create a(n) Contact Request
*CustomSignatureDefinitionsApi* | [**activate**](docs/CustomSignatureDefinitionsApi.md#activate) | **PATCH** /api/v2/custom_signature_definitions/{custom_signature_definition_id}/activate.json_api | A successful call to this API activates and returns a specific custom signature definition identified by the id parameter. The definition must have a status of editable to be activated.
*CustomSignatureDefinitionsApi* | [**archive**](docs/CustomSignatureDefinitionsApi.md#archive) | **PATCH** /api/v2/custom_signature_definitions/{custom_signature_definition_id}/archive.json_api | A successful call to this API archives and returns a specific custom signature definition identified by the id parameter. The definition must have a status of active to be archived.
*CustomSignatureDefinitionsApi* | [**create**](docs/CustomSignatureDefinitionsApi.md#create) | **POST** /api/v2/custom_signature_definitions.json_api | Create a(n) Custom Signature/Definition
*CustomSignatureDefinitionsApi* | [**destroy**](docs/CustomSignatureDefinitionsApi.md#destroy) | **DELETE** /api/v2/custom_signature_definitions/{id}.json_api | Remove a(n) CustomSignature::Definition
*CustomSignatureDefinitionsApi* | [**list**](docs/CustomSignatureDefinitionsApi.md#list) | **PUT** /api/v2/custom_signature_definitions.json_api | Get a list of Custom Signature/Definitions
*CustomSignatureDefinitionsApi* | [**show**](docs/CustomSignatureDefinitionsApi.md#show) | **GET** /api/v2/custom_signature_definitions/{id}.json_api | Show a single Custom Signature/Definition
*CustomSignatureDefinitionsApi* | [**update**](docs/CustomSignatureDefinitionsApi.md#update) | **PATCH** /api/v2/custom_signature_definitions/{id}.json_api | Update a(n) Custom Signature/Definition
*CustomSignatureResultsApi* | [**alerts**](docs/CustomSignatureResultsApi.md#alerts) | **GET** /api/v2/custom_signature_results/{custom_signature_result_id}/alerts.json_api | Returns the alerts for a given result. Note that this format is slightly different than the standard alert format. A successful call to this API returns a list of alerts for the custom signature result identified by the id parameter.
*CustomSignatureResultsApi* | [**create**](docs/CustomSignatureResultsApi.md#create) | **POST** /api/v2/custom_signature_results.json_api | Create a(n) Custom Signature/Result
*CustomSignatureResultsApi* | [**list**](docs/CustomSignatureResultsApi.md#list) | **PUT** /api/v2/custom_signature_results.json_api | Get a list of Custom Signature/Results
*CustomSignatureResultsApi* | [**show**](docs/CustomSignatureResultsApi.md#show) | **GET** /api/v2/custom_signature_results/{id}.json_api | Show a single Custom Signature/Result
*CustomSignaturesApi* | [**create**](docs/CustomSignaturesApi.md#create) | **POST** /api/v2/custom_signatures.json_api | Create a(n) Custom Signature
*CustomSignaturesApi* | [**destroy**](docs/CustomSignaturesApi.md#destroy) | **DELETE** /api/v2/custom_signatures/{id}.json_api | Remove a(n) CustomSignature
*CustomSignaturesApi* | [**list**](docs/CustomSignaturesApi.md#list) | **PUT** /api/v2/custom_signatures.json_api | Get a list of Custom Signatures
*CustomSignaturesApi* | [**show**](docs/CustomSignaturesApi.md#show) | **GET** /api/v2/custom_signatures/{id}.json_api | Show a single Custom Signature
*CustomSignaturesApi* | [**update**](docs/CustomSignaturesApi.md#update) | **PATCH** /api/v2/custom_signatures/{id}.json_api | Update a(n) Custom Signature
*ExternalAccountDisabledSignaturesApi* | [**create**](docs/ExternalAccountDisabledSignaturesApi.md#create) | **POST** /api/v2/external_accounts/{external_account_id}/disabled_signatures.json_api | A successful call to this API will disable a signature for an external account.
*ExternalAccountDisabledSignaturesApi* | [**destroy**](docs/ExternalAccountDisabledSignaturesApi.md#destroy) | **DELETE** /api/v2/external_accounts/{external_account_id}/disabled_signatures.json_api | A successful call to this API will remove a signature from the disabled signature list on an external account.
*ExternalAccountDisabledSignaturesApi* | [**list**](docs/ExternalAccountDisabledSignaturesApi.md#list) | **GET** /api/v2/external_accounts/{external_account_id}/disabled_signatures.json_api | A successful call to this API returns all the disabled signatures of the associated external account, identified by the external_account_id parameter.
*ExternalAccountDisabledSignaturesApi* | [**update**](docs/ExternalAccountDisabledSignaturesApi.md#update) | **PATCH** /api/v2/external_accounts/{external_account_id}/disabled_signatures.json_api | A successful call to this API will update the disabled signatures on an external account.
*ExternalAccountUserAttributionChannelsApi* | [**create**](docs/ExternalAccountUserAttributionChannelsApi.md#create) | **POST** /api/v2/external_accounts/{external_account_id}/user_attribution/channel.json_api | A successful call to this API will create a User Attribution Channel for an external account.
*ExternalAccountUserAttributionChannelsApi* | [**destroy**](docs/ExternalAccountUserAttributionChannelsApi.md#destroy) | **DELETE** /api/v2/external_accounts/{external_account_id}/user_attribution/channel.json_api | A successful call to this API will remove the User Attribution Channel for an external account.
*ExternalAccountUserAttributionChannelsApi* | [**show**](docs/ExternalAccountUserAttributionChannelsApi.md#show) | **GET** /api/v2/external_accounts/{external_account_id}/user_attribution/channel.json_api | A successful call to this API will show the User Attribution Channel of an external account.
*ExternalAccountUserAttributionsApi* | [**update**](docs/ExternalAccountUserAttributionsApi.md#update) | **PATCH** /api/v2/external_accounts/{external_account_id}/user_attribution.json_api | A successful call to this API will update the user attributions on an external account.
*ExternalAccountsApi* | [**create**](docs/ExternalAccountsApi.md#create) | **POST** /api/v2/external_accounts.json_api | Create a(n) External Account
*ExternalAccountsApi* | [**destroy**](docs/ExternalAccountsApi.md#destroy) | **DELETE** /api/v2/external_accounts/{id}.json_api | Remove a(n) ExternalAccount
*ExternalAccountsApi* | [**list**](docs/ExternalAccountsApi.md#list) | **PUT** /api/v2/external_accounts.json_api | Get a list of External Accounts
*ExternalAccountsApi* | [**show**](docs/ExternalAccountsApi.md#show) | **GET** /api/v2/external_accounts/{id}.json_api | Show a single External Account
*ExternalAccountsApi* | [**update**](docs/ExternalAccountsApi.md#update) | **PATCH** /api/v2/external_accounts/{id}.json_api | Update a(n) External Account
*MetadataApi* | [**for_alert**](docs/MetadataApi.md#for_alert) | **GET** /api/v2/alerts/{alert_id}/metadata.json_api | Show the metadata for an alert
*MetadataApi* | [**show**](docs/MetadataApi.md#show) | **GET** /api/v2/metadata/{id}.json_api | Show a single Metadata
*OrganizationsApi* | [**list**](docs/OrganizationsApi.md#list) | **PUT** /api/v2/organizations.json_api | Get a list of Organizations
*OrganizationsApi* | [**show**](docs/OrganizationsApi.md#show) | **GET** /api/v2/organizations/{id}.json_api | Show a single Organization
*OrganizationsApi* | [**update**](docs/OrganizationsApi.md#update) | **PATCH** /api/v2/organizations/{id}.json_api | Update a(n) Organization
*PermissionsApi* | [**list**](docs/PermissionsApi.md#list) | **GET** /api/v2/permissions.json_api | This API provides a list of all the permissions that the current user has
*RegionsApi* | [**list**](docs/RegionsApi.md#list) | **PUT** /api/v2/regions.json_api | Get a list of Regions
*RegionsApi* | [**show**](docs/RegionsApi.md#show) | **GET** /api/v2/regions/{id}.json_api | Show a single Region
*ReportIntegrationsApi* | [**create**](docs/ReportIntegrationsApi.md#create) | **POST** /api/v2/reports/export/integrations.json_api | Export all alerts on reports to an integration
*ReportsApi* | [**create**](docs/ReportsApi.md#create) | **POST** /api/v2/reports.json_api | Create a(n) Report
*ReportsApi* | [**list**](docs/ReportsApi.md#list) | **PUT** /api/v2/reports.json_api | Get a list of Reports
*ReportsApi* | [**show**](docs/ReportsApi.md#show) | **GET** /api/v2/reports/{id}.json_api | Show a single Report
*RolesApi* | [**list**](docs/RolesApi.md#list) | **GET** /api/v2/roles.json_api | Get a list of Roles
*RolesApi* | [**show**](docs/RolesApi.md#show) | **GET** /api/v2/roles/{id}.json_api | Show a single Role
*ScanIntervalsApi* | [**create**](docs/ScanIntervalsApi.md#create) | **POST** /api/v2/scan_intervals.json_api | Create a(n) Scan Interval
*ScanIntervalsApi* | [**destroy**](docs/ScanIntervalsApi.md#destroy) | **DELETE** /api/v2/scan_intervals/{id}.json_api | Remove a(n) ScanInterval
*ScanIntervalsApi* | [**list**](docs/ScanIntervalsApi.md#list) | **GET** /api/v2/external_accounts/{external_account_id}/scan_intervals.json_api | Get a list of Scan Intervals
*ScanIntervalsApi* | [**show**](docs/ScanIntervalsApi.md#show) | **GET** /api/v2/scan_intervals/{id}.json_api | Show a single Scan Interval
*ScanIntervalsApi* | [**update**](docs/ScanIntervalsApi.md#update) | **PATCH** /api/v2/scan_intervals/{id}.json_api | Update a(n) Scan Interval
*ServicesApi* | [**list**](docs/ServicesApi.md#list) | **PUT** /api/v2/services.json_api | Get a list of Services
*ServicesApi* | [**show**](docs/ServicesApi.md#show) | **GET** /api/v2/services/{id}.json_api | Show a single Service
*SignatureCustomRiskLevelsApi* | [**create**](docs/SignatureCustomRiskLevelsApi.md#create) | **POST** /api/v2/signature_custom_risk_levels.json_api | Create a(n) Signature Custom Risk Level
*SignatureCustomRiskLevelsApi* | [**destroy**](docs/SignatureCustomRiskLevelsApi.md#destroy) | **DELETE** /api/v2/signature_custom_risk_levels/{id}.json_api | Remove a(n) SignatureCustomRiskLevel
*SignatureCustomRiskLevelsApi* | [**list**](docs/SignatureCustomRiskLevelsApi.md#list) | **GET** /api/v2/external_accounts/{external_account_id}/signature_custom_risk_levels.json_api | Get a list of Signature Custom Risk Levels
*SignatureCustomRiskLevelsApi* | [**show**](docs/SignatureCustomRiskLevelsApi.md#show) | **GET** /api/v2/signature_custom_risk_levels/{id}.json_api | Show a single Signature Custom Risk Level
*SignatureCustomRiskLevelsApi* | [**update**](docs/SignatureCustomRiskLevelsApi.md#update) | **PATCH** /api/v2/signature_custom_risk_levels/{id}.json_api | Update a(n) Signature Custom Risk Level
*SignaturesApi* | [**list**](docs/SignaturesApi.md#list) | **PUT** /api/v2/signatures.json_api | Get a list of Signatures
*SignaturesApi* | [**run**](docs/SignaturesApi.md#run) | **POST** /api/v2/signatures/{id}/run.json_api | Run a Signature
*SignaturesApi* | [**show**](docs/SignaturesApi.md#show) | **GET** /api/v2/signatures/{id}.json_api | Show a single Signature
*StatsApi* | [**for_compliance_controls**](docs/StatsApi.md#for_compliance_controls) | **GET** /api/v2/stats/{stat_id}/compliance_controls.json_api | A successful call to this API returns all the stats of all the compliance controls for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all compliance controls for the selected hour.
*StatsApi* | [**for_custom_signatures**](docs/StatsApi.md#for_custom_signatures) | **GET** /api/v2/stats/{stat_id}/custom_signatures.json_api | A successful call to this API returns all the stats of all the custom signatures for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all custom_signatures for the selected hour.
*StatsApi* | [**for_regions**](docs/StatsApi.md#for_regions) | **GET** /api/v2/stats/{stat_id}/regions.json_api | A successful call to this API returns all the stats of all the regions for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all regions for the selected hour.
*StatsApi* | [**for_report**](docs/StatsApi.md#for_report) | **GET** /api/v2/reports/{report_id}/stats.json_api | A successful call to this API returns all the stats of all the alerts for a report identified by the report_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all regions for the selected hour.
*StatsApi* | [**for_services**](docs/StatsApi.md#for_services) | **GET** /api/v2/stats/{stat_id}/services.json_api | A successful call to this API returns all the stats of all the services for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all services for the selected hour.
*StatsApi* | [**for_signatures**](docs/StatsApi.md#for_signatures) | **GET** /api/v2/stats/{stat_id}/signatures.json_api | A successful call to this API returns all the stats of all the signatures for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all signatures for the selected hour.
*StatsApi* | [**latest_for_teams**](docs/StatsApi.md#latest_for_teams) | **GET** /api/v2/stats/latest_for_teams.json_api | A successful call to this API returns all the stats for the most recent report of each team accessible by the given API key
*StatsApi* | [**show**](docs/StatsApi.md#show) | **GET** /api/v2/stats/{id}.json_api | Show a single Stat
*SubOrganizationsApi* | [**create**](docs/SubOrganizationsApi.md#create) | **POST** /api/v2/sub_organizations.json_api | Create a(n) Sub Organization
*SubOrganizationsApi* | [**destroy**](docs/SubOrganizationsApi.md#destroy) | **DELETE** /api/v2/sub_organizations/{id}.json_api | Remove a(n) SubOrganization
*SubOrganizationsApi* | [**list**](docs/SubOrganizationsApi.md#list) | **PUT** /api/v2/sub_organizations.json_api | Get a list of Sub Organizations
*SubOrganizationsApi* | [**show**](docs/SubOrganizationsApi.md#show) | **GET** /api/v2/sub_organizations/{id}.json_api | Show a single Sub Organization
*SubOrganizationsApi* | [**update**](docs/SubOrganizationsApi.md#update) | **PATCH** /api/v2/sub_organizations/{id}.json_api | Update a(n) Sub Organization
*SuppressionsApi* | [**deactivate**](docs/SuppressionsApi.md#deactivate) | **PATCH** /api/v2/suppressions/{id}/deactivate.json_api | A successful call to this API will deactivate a suppression identified by the id parameter.
*SuppressionsApi* | [**list**](docs/SuppressionsApi.md#list) | **PUT** /api/v2/suppressions.json_api | Get a list of Suppressions
*SuppressionsApi* | [**show**](docs/SuppressionsApi.md#show) | **GET** /api/v2/suppressions/{id}.json_api | Show a single Suppression
*SuppressionsApi* | [**suppress_region**](docs/SuppressionsApi.md#suppress_region) | **POST** /api/v2/suppressions/regions.json_api | A successful call to this API creates a new region suppression for the supplied regions . The body of the request must contain a json api compliant hash of attributes with type suppression/regions.
*SuppressionsApi* | [**suppress_region_from_alert**](docs/SuppressionsApi.md#suppress_region_from_alert) | **POST** /api/v2/suppressions/alert/{alert_id}/regions.json_api | A successful call to this API creates a new signature suppression based on the supplied alert_id. The body of the request must contain a json api compliant hash of attributes with type suppression/regions.
*SuppressionsApi* | [**suppress_signature**](docs/SuppressionsApi.md#suppress_signature) | **POST** /api/v2/suppressions/signatures.json_api | A successful call to this API creates a new signature suppression for the supplied signature_ids or custom_signature_ids. The body of the request must contain a json API compliant hash of attributes with type suppression/signatures.
*SuppressionsApi* | [**suppress_signature_from_alert**](docs/SuppressionsApi.md#suppress_signature_from_alert) | **POST** /api/v2/suppressions/alert/{alert_id}/signatures.json_api | A successful call to this API creates a new signature suppression based on the supplied alert_id. The body of the request must contain a json api compliant hash of attributes with type suppression/signatures.
*SuppressionsApi* | [**suppress_unique_identifier_from_alert**](docs/SuppressionsApi.md#suppress_unique_identifier_from_alert) | **POST** /api/v2/suppressions/alert/{alert_id}/unique_identifiers.json_api | A successful call to this API creates a new unique identifier suppression based on the supplied alert_id. The body of the request must contain a json api compliant hash of attributes with type suppression/signatures.
*TagsApi* | [**list**](docs/TagsApi.md#list) | **GET** /api/v2/alerts/{alert_id}/tags.json_api | Get a list of Tags
*TagsApi* | [**show**](docs/TagsApi.md#show) | **GET** /api/v2/tags/{id}.json_api | Show a single Tag
*TeamsApi* | [**create**](docs/TeamsApi.md#create) | **POST** /api/v2/teams.json_api | Create a(n) Team
*TeamsApi* | [**destroy**](docs/TeamsApi.md#destroy) | **DELETE** /api/v2/teams/{id}.json_api | Remove a(n) Team
*TeamsApi* | [**list**](docs/TeamsApi.md#list) | **PUT** /api/v2/teams.json_api | Get a list of Teams
*TeamsApi* | [**show**](docs/TeamsApi.md#show) | **GET** /api/v2/teams/{id}.json_api | Show a single Team
*TeamsApi* | [**update**](docs/TeamsApi.md#update) | **PATCH** /api/v2/teams/{id}.json_api | Update a(n) Team
*TimeZonesApi* | [**list**](docs/TimeZonesApi.md#list) | **GET** /api/v2/time_zones.json_api | A successful call to this API returns a list of time zones.
*UsersApi* | [**create**](docs/UsersApi.md#create) | **POST** /api/v2/users.json_api | Create a(n) User
*UsersApi* | [**destroy**](docs/UsersApi.md#destroy) | **DELETE** /api/v2/users/{id}.json_api | Remove a(n) User
*UsersApi* | [**list**](docs/UsersApi.md#list) | **PUT** /api/v2/users.json_api | Get a list of Users
*UsersApi* | [**show**](docs/UsersApi.md#show) | **GET** /api/v2/users/{id}.json_api | Show a single User
*UsersApi* | [**update**](docs/UsersApi.md#update) | **PATCH** /api/v2/users/{id}.json_api | Update a(n) User


## Documentation For Models

 - [Alert](docs/Alert.md)
 - [AuditLog](docs/AuditLog.md)
 - [AuditLogFile](docs/AuditLogFile.md)
 - [Channel](docs/Channel.md)
 - [CloudTrailEvent](docs/CloudTrailEvent.md)
 - [ComplianceControl](docs/ComplianceControl.md)
 - [ComplianceDomain](docs/ComplianceDomain.md)
 - [ComplianceStandard](docs/ComplianceStandard.md)
 - [ContactRequest](docs/ContactRequest.md)
 - [CustomSignature](docs/CustomSignature.md)
 - [CustomSignatureDefinition](docs/CustomSignatureDefinition.md)
 - [CustomSignatureResult](docs/CustomSignatureResult.md)
 - [CustomSignatureResultAlert](docs/CustomSignatureResultAlert.md)
 - [ExternalAccount](docs/ExternalAccount.md)
 - [MessageObject](docs/MessageObject.md)
 - [MetaMessageObject](docs/MetaMessageObject.md)
 - [Metadata](docs/Metadata.md)
 - [Organization](docs/Organization.md)
 - [PaginatedCollection](docs/PaginatedCollection.md)
 - [Region](docs/Region.md)
 - [Report](docs/Report.md)
 - [Role](docs/Role.md)
 - [ScanInterval](docs/ScanInterval.md)
 - [Service](docs/Service.md)
 - [Signature](docs/Signature.md)
 - [SignatureCustomRiskLevel](docs/SignatureCustomRiskLevel.md)
 - [Stat](docs/Stat.md)
 - [StatsComplianceControl](docs/StatsComplianceControl.md)
 - [StatsCustomSignature](docs/StatsCustomSignature.md)
 - [StatsRegion](docs/StatsRegion.md)
 - [StatsService](docs/StatsService.md)
 - [StatsSignature](docs/StatsSignature.md)
 - [SubOrganization](docs/SubOrganization.md)
 - [Suppression](docs/Suppression.md)
 - [Tag](docs/Tag.md)
 - [Team](docs/Team.md)
 - [TimeZone](docs/TimeZone.md)
 - [User](docs/User.md)
 - [UserPermission](docs/UserPermission.md)

