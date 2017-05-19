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
					    //location.href = this.$target.attr('href');
						$.get('delete',function (data) {
							var msg = data.toString()
							if(msg=='删除成功'){
							alert(msg)
								window.location.href='/testapp/article/all/'
								//location.href=this.$target.attr('/testapp/article/all/');
							}

                        })
					}
				},
				'No'	: {
					'class'	: 'gray',
					'action': function(){}	// Nothing to do in this case. You can as well omit the action property.
				}
			}
            });
        });
