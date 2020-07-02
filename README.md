Archiware P5 Module
====================

Reports Archiware P5 data on the clients.

Notes
-----

Archiware provides data management software for backup, synchronization & archiving for small-medium sized businesses & the media/entertainment industry.

https://www.archiware.com/

Table Schema
-----

* license resources  - VARCHAR(255) - Names of all available resources
* ArchivePlan        - VARCHAR(255) - If ArchivePlan is installed
* BackupPlan         - VARCHAR(255) - If BackupPlan is installed
* SyncPlan           - VARCHAR(255) - If SyncPlan is installed   
* Backup2Go          - VARCHAR(255) - If Backup2Go is installed
* Client             - VARCHAR(255) - If Client is installed
* ThinClient         - VARCHAR(255) - If ThinClient is installed
* VirtClient         - VARCHAR(255) - If VirtClient is installed
* Device             - VARCHAR(255) - If Device is installed
* Jukebox            - VARCHAR(255) - If Jukebox is installed
* DesktopLinks       - VARCHAR(255) - If ArchivePlan is installed
* hostid             - (INT11)      - Client ID number
* port               - (INT11)      - Port Server is running on
* platform           - VARCHAR(255) - OS client is running on
* lexxvers           - VARCHAR(255) - P5 Server Version
* uptime             - VARCHAR(255) - Time client has been running in hours
