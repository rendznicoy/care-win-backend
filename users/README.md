# Users
The User entity represents system administrators with varying levels of access control. Each user is assigned an `auth_level` based on their role in managing election data. Additionally, users can have specific `roles` that grant extra permissions within the system. The `roles` attribute is useful for further scalability usages.

## JSON Format

|Name   |Type   |Read-only  |Mandatory  |Description    |
|---    |---    |---        |---        |---            |
|active |boolean|true       |false      |`false` if the user has been deleted|
|details|string |false      |false      |Any details you want to store about the user, such as an address|
|email  |string |false      |false      |Primary email address used for authentication|
|id     |string |true       |false      |Unique user identifier|
|name   |string |false      |true       |Full name of the user|
|phone  |string |false      |false      |Contact number|
|photo_url|string|false     |false      |A URL pointing to the user's profile picture|
|role   |integer |false     |false      |The user's role id. 0 for a precinct-level admin, 1 for barangay-level admin, and 2 for city-level admin|
|updated_at|string|true     |false      |The time the user was last updated|