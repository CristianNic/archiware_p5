<?php

// Database seeder
// Please visit https://github.com/fzaninotto/Faker for more options

/** @var \Illuminate\Database\Eloquent\Factory $factory */
$factory->define(Archiware_p5_model::class, function (Faker\Generator $faker) {

    return [
        'host_id' => $faker->word(),
        'port' => $faker->randomNumber($nbDigits = 4, $strict = false),
        'platform' => $faker->word(),
        'p5_version' => $faker->word(),
        //'uptime' => $faker->word(),
        'uptime' => $faker->dateTimeBetween('-12 days')->format('U'),
        'archive_plan' => $faker->word(),
        'backup_plan' => $faker->word(),
        'sync_plan' => $faker->word(),
        'backup2go' => $faker->word(),
        'client' => $faker->word(),
        'thin_client' => $faker->word(),
        'virtual_client' => $faker->word(),
        'device' => $faker->word(),
        'jukebox' => $faker->word(),
        'desktop_links' => $faker->word(),
    ];
});
