(function(){
	var app = angular.module('assignment_view', [ ]);
    var course_list = ['DSPD','DMGT','OS'];

    var assignment_object = [
                        {
                            'name' : 'Ass-1',
                            'course_name' : 'DMGT',
                            'deadline' : '01-05-2016',
                            'time_uploaded' : '08-07-2015',
                            'assign_id' : '1',
                            'time_modified' : '08-07-1998',
                            
                        },
                        {
                            'name' : 'Ass-2',
                            'course_name' : 'DMGT',
                            'deadline' : '01-05-2016',
                            'time_uploaded' : '08-07-2015',
                            'assign_id' : '1',
                            'time_modified' : '08-07-1998',
                        },
                        {
                            'name' : 'Ass-1',
                            'course_name' : 'DMGT',
                            'deadline' : '01-06-2016',
                            'time_uploaded' : '08-09-2015',
                            'assign_id' : '2',
                            'time_modified' : '08-07-1998',
                        },
                        {
                            'name' : 'Ass-1',
                            'course_name' : 'DSPD',
                            'deadline' : '01-06-2016',
                            'time_uploaded' : '08-09-2015',
                            'assign_id' : '3',
                            'time_modified' : '08-07-1998',
                        },
                        {
                            'name' : 'Ass-1',
                            'course_name' : 'OS',
                            'deadline' : '01-06-2016',
                            'time_uploaded' : '08-09-2015',
                            'assign_id' : '4',
                            'time_modified' : '08-07-1998',
                        },
                        ];
    

    app.controller('ProfController',function($scope){
           this.course_list = course_list;
           this.assgn_list=assignment_object;
           this.assignment={};
           this.show_assignments = function(){
        	   this.assgn_list=[];
        	   var len=assignment_object.length;
        	   //alert(len);
        	   for (var i=0;i<len;i++){
        		   if ((assignment_object[i].course_name.localeCompare($scope.selectedCourse)==0)){
        			   this.assgn_list.push(
        					   {
        						   name : assignment_object[i].name,
        						   deadline : assignment_object[i].deadline,
        						   assign_id : assignment_object[i].assign_id,
        						   course_name : assignment_object[i].course_name,
        						   time_modified : assignment_object[i].time_modified,
        						   time_uploaded : assignment_object[i].time_uploaded
        					   }
        					   );		   
        		   }
        	   }
           };
           this.setAssign = function(assign){
        	   //alert('here');
        	   this.assignment=assign;
        	   //$( "#opener" ).click(function() {
     		      $( "#dialog" ).dialog( "open" );
     		    //});
        	   this.assign_id = assign_id;
           };
    });

})()