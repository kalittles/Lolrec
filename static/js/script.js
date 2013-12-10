/* Script for CSCE 470 search engine
 *
 */

var tweet_template = _.template($('#tweet_template').html(),null,{variable:'t'});
var result_template = _.template($('#result_template').html());
var alert_template = _.template($('#alert_template').html());

$('#tweetsearch form').submit(function(ev) {
    var q = $(this).find('input[name=query]').val();
    ajax_search(q);
    return false;
});


function ajax_search(q) {
  $.ajax('/search',{
      data:{q:q},
      timeout:15000,
      success: function(data) {
        var result_div = $('#tweetsearch .results');
        result_div.empty();
        result_div.show();
        result_div.append($(result_template(data)));
        var tweet_divs = _.map(data.tweets, tweet_template);
        result_div.append(tweet_divs.join(''));
      },
      error: function(jqXHR,textStatus,errorThrown) {
        var error;
        if(textStatus=='error') {
          if(jqXHR.status==0)
            error = "Could not connect to server. Try running ./serve.py.";
          else
            error = jqXHR.status+" : "+errorThrown;
        } else {
          error = textStatus;
        }

        var alert = alert_template({error:error});
        $('#tweetsearch form').after(alert);
        $('#tweetsearch .results').hide();
      },
      dataType: 'json',
  });
}

