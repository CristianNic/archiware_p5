<?php

/**
 * archiware_p5 class
 *
 * @package munkireport
 * @author CristianNic
 **/
class Archiware_p5_controller extends Module_controller
{

		/*** Protect methods with auth! ****/
		function __construct()
    {
        // Store module path
        $this->module_path = dirname(__FILE__);
    }

    /**
     * Get archiware_p5 information for serial_number
     *
     * @param string $serial serial number
     **/
/**
*    public function get_data($serial_number = '')
*    {
*        jsonView(
*            Archiware_p5_model::select('archiware_p5.*')
*            ->whereSerialNumber($serial_number)
*            ->filter()
*            ->limit(1)
*            ->first()
*            ->toArray()
*        );
*    }
**/

		function index()
		{
			echo "You've loaded the firewall module!";
		}

		public function get_archiware_p5()
		{
				jsonView(
								Archiware_p5_model::selectRaw('host_id, count(*) AS count')
								->filter()
								->groupBy('host_id')
								->orderBy('count', 'desc')
								->get()
								->toArray()
						);
		}

		public function get_data($serial_number = '')
    {
        jsonView(
            Archiware_p5_model::selectRaw('host_id, port, platform, p5_version, uptime, archive_plan, backup_plan, sync_plan, backup2go, client, thin_client, virtual_client, device, jukebox, desktop_links')
                ->whereSerialNumber($serial_number)
                ->filter()
                ->get()
                ->toArray()
        );
    }

    public function get_list($column = '')
    {
        jsonView(
            Archiware_p5_model::select($column . ' AS label')
                ->selectRaw('count(*) AS count')
                ->filter()
                ->groupBy($column)
                ->orderBy('count', 'desc')
                ->get()
                ->toArray()
        );
    }

} // End class Archiware_p5_controller
