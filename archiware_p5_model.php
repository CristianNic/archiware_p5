<?php

use munkireport\models\MRModel as Eloquent;

class Archiware_p5_model extends Eloquent
{
    protected $table = 'archiware_p5';

    protected $hidden = ['id', 'serial_number'];

    protected $fillable = [
      'serial_number',
      'archive_plan',
      'backup_plan',
      'sync_plan',
      'backup2go',
      'client',
      'thin_client',
      'virtual_client',
      'device',
      'jukebox',
      'desktop_links',
      'host_id',
      'port',
      'platform',
      'p5_version',
      'uptime',

    ];
}
