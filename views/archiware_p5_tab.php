<div id="archiware_p5-tab"></div>
<h2 data-i18n="archiware_p5.title"></h2>

<table id="archiware_p5-tab-table"></table>

<script>
$(document).on('appReady', function(){
    $.getJSON(appUrl + '/module/archiware_p5/get_data/' + serialNumber, function(data){
        var table = $('#archiware_p5-tab-table');
        $.each(data, function(key,val){
            var th = $('<th>').text(i18n.t('archiware_p5.column.' + key));
            var td = $('<td>').text(val);
            table.append($('<tr>').append(th, td));
        });
    });
});
</script>
