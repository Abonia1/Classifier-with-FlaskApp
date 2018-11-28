
$(function() {
    $('#text').on('input',function() {
   //$('button').click(function() {

        $.ajax({
            url: '/predictions',
            data: $('#text').serialize(),
            type: 'POST',
            success: function(category) {
                 //console.log(category)
                // $('#category').html(response);
                document.getElementById('category').innerHTML=category;
                //console.log(document.getElementById('category').innerHTML);

            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
