Archiware P5 Module
====================

Reports Archiware P5 data on the clients.

Notes
-----

Archiware provides data management software for backup, synchronization & archiving for small-medium sized businesses & the media/entertainment industry.

https://www.archiware.com/

Table Schema
-----

* Host ID         - VARCHAR(255) - Client ID number
* Port            - VARCHAR(255) - Port Server is running on
* Platform        - VARCHAR(255) - Platform client is running on (linux, freeBSD, windows, macOS)
* P5 Version      - VARCHAR(255) - P5 software Version
* Uptime          - VARCHAR(255) - Amount of time P5 software has been running
* ArchivePlan     - VARCHAR(255) - If ArchivePlan is licensed and amount of licenses available
* Backup Plan     - VARCHAR(255) - If BackupPlan is licensed and amount of licenses available
* Sync Plan       - VARCHAR(255) - If SyncPlan is licensed and amount of licenses available  
* Backup2Go       - VARCHAR(255) - If Backup2Go is licensed and amount of licenses available
* Client          - VARCHAR(255) - If Client is licensed and amount of licenses available
* Thin Client     - VARCHAR(255) - If ThinClient is licensed and amount of licenses available
* Virtual Client  - VARCHAR(255) - If VirtClient is licensed and amount of licenses available
* Device          - VARCHAR(255) - If Device is licensed and amount of licenses available
* Jukebox         - VARCHAR(255) - If Jukebox is licensed and amount of licenses available
* Desktop Links   - VARCHAR(255) - If Archive App is installed and amount of licenses available
