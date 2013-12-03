jQuery(document).ready(function($) {
    $('#form').submit(function() {

        var output = $('#output');
        output.html('<img src="/static/flask/img/loading.gif" alt="Loading..." />');

        var formData = $(this).serialize();
        var url = '/team-generator/generate';

        $.post(url, formData, function(data, textStatus) {
            var keys = [];
            for(var key in data) {
                keys.push(key);
            }
            keys.sort();

            output.html("<h2>Teams:</h2>");

            for(var i = 0; i < keys.length; i ++) {
                output.append('<h3 class="team-name">' + keys[i] + '</h3><ul>');
                for(var j = 0; j < data[keys[i]].length; j++) {
                    output.append('<li>' + data[keys[i]][j] + '</li>');
                }
                output.append('</ul>');
            }

        }, 'json')
        .fail(function(xhr, textStatus, errorThrown) {
            output.html('<span class="error">There was a problem generating the teams. Please try again.</span>');
        });

        return false;
    });
});
