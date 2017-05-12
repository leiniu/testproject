$(document).ready(function(){
        $('.deletelink').confirm({
                title: 'Wraning!',
                content: 'Are you sure delete this case?',
                ok:'YES',
                concel:'NO',
                'buttons'	: {
				'Yes'	: {
					'class'	: 'blue',
					'action': function(){
					    location.href = this.$target.attr('href');
					}
				},
				'No'	: {
					'class'	: 'gray',
					'action': function(){}	// Nothing to do in this case. You can as well omit the action property.
				}
			}
            });
        });