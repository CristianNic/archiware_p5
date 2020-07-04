<?php
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Capsule\Manager as Capsule;

class ArchiwareP5Init extends Migration
{
    public function up()
    {
        $capsule = new Capsule();
        $capsule::schema()->create('archiware_p5', function (Blueprint $table) {
            $table->increments('id');
            $table->string('serial_number');
            $table->string('archive_plan')->nullable();
            $table->string('backup_plan')->nullable();
            $table->string('sync_plan')->nullable();
            $table->string('backup2go')->nullable();
            $table->string('client')->nullable();
            $table->string('thin_client')->nullable();
            $table->string('virtual_client')->nullable();
            $table->string('device')->nullable();
            $table->string('jukebox')->nullable();
            $table->string('desktop_links')->nullable();
            $table->string('host_id')->nullable();
            $table->string('port')->nullable();
            $table->string('platform')->nullable();
            $table->string('p5_version')->nullable();
            $table->string('uptime')->nullable();

            $table->unique('serial_number');
            $table->index('archive_plan');
            $table->index('backup_plan');
            $table->index('sync_plan');
            $table->index('backup2go');
            $table->index('client');
            $table->index('thin_client');
            $table->index('virtual_client');
            $table->index('device');
            $table->index('jukebox');
            $table->index('desktop_links');
            $table->index('host_id');
            $table->index('port');
            $table->index('platform');
            $table->index('p5_version');
            $table->index('uptime');

        });
    }
    
    public function down()
    {
        $capsule = new Capsule();
        $capsule::schema()->dropIfExists('archiware_p5');
    }
}
