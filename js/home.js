function toggleDrawer(){
	var layout = document.querySelector('.mdl-layout');
	layout.MaterialLayout.toggleDrawer();
}

function appendList(e){
	// table title
	var table_title = (e.replace(".json","")).replace("_"," ");

	var url = "./done/";
	url += e;
	$.get(url,function (data){
		var htm_header = "<h2>"+table_title+"</h2><table class='mdl-data-table mdl-js-data-table list-name-company'> \
						  <thead> \
						    <tr> \
						      <th class='mdl-data-table__cell--non-numeric'>Name</th> \
						      <th>Company</th> \
						    </tr> \
						  </thead> \
						  <tbody>";
		all_rows = htm_header;
		for(var i in data){
			var name = "";
			name = data[i]['_name'];
			var companyList = data[i]['_company'];
			// company might be empty
			try{
				var currentCompany = companyList[0]['company'];	
			}
			catch(err){
				var currentCompany = "";	
			}
			if(name == undefined || currentCompany == ""){
				continue;
			}
			else{
				var td = "<td class='mdl-data-table__cell--non-numeric'>";
				var tmp = "<tr>"+td+name+"</td>"+"<td>"+currentCompany+"</td></tr>";
				all_rows += tmp;	
			}
		}	
		all_rows += "</tbody> \
					 </table>";
		$('#tab-1>div').append(all_rows);
    });    
}

$(document).on('click','.mdl-navigation__link',function(e){
	// close drawer on click
	toggleDrawer();
	// show/hide content page
	$('.page-content').addClass('hide-element');
	var href = $(this).attr('href');
	href += '>div';
	$(href).removeClass('hide-element');
	// show/hide content page ends

});

$(document).ready(function(e){
	// need to call function to append list {name - company} of different batches
	// filename should be in the format TABLE_TIITLE.json
	appendList('2011-2015.json');
	appendList('2005-2009.json');
});