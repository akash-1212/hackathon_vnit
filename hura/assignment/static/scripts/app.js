(function(){
	var app = angular.module('assignment_view', [ ]);
    var prof_course = [
                       {
                    	   'course_name' : 'All',
                    	   'prof_name' : ['All']
                       },
                       {
                            'course_name' : 'DSPD',
                            'prof_name' : ['Keskar']
                        },
                        {
                            'course_name' : 'OS',
                            'prof_name' : ['Tiwari']
                        },
                        {
                            'course_name' : 'DMGT',
                            'prof_name' : ['dmgt1','dmgt2']
                        },

                        ];

    var assignment_object = [
                        {
                            'name' : 'Ass-1',
                            'course_name' : 'DMGT',
                            'prof_name' : 'dmgt1',
                            'deadline' : '01-05-2016',
                            'time_uploaded' : '08-07-2015',
                            'assign_id' : '1',
                            'status' : 'yes'
                        },
                        {
                            'name' : 'Ass-2',
                            'course_name' : 'DMGT',
                            'prof_name' : 'dmgt1',
                            'deadline' : '01-05-2016',
                            'time_uploaded' : '08-07-2015',
                            'assign_id' : '1',
                            'status' : 'yes'
                        },
                        {
                            'name' : 'Ass-1',
                            'course_name' : 'DMGT',
                            'prof_name' : 'dmgt2',
                            'deadline' : '01-06-2016',
                            'time_uploaded' : '08-09-2015',
                            'assign_id' : '2',
                            'status' : 'no'
                        },
                        {
                            'name' : 'Ass-1',
                            'course_name' : 'DSPD',
                            'prof_name' : 'Keskar',
                            'deadline' : '01-06-2016',
                            'time_uploaded' : '08-09-2015',
                            'assign_id' : '3',
                            'status' : 'yes'
                        },
                        {
                            'name' : 'Ass-1',
                            'course_name' : 'OS',
                            'prof_name' : 'Tiwari',
                            'deadline' : '01-06-2016',
                            'time_uploaded' : '08-09-2015',
                            'assign_id' : '4',
                            'status' : 'yes'
                        },
                        ];
    

    app.controller('ProfCourseController',function($scope){
           this.prof_course = prof_course;
           this.prof_course_list = _.pluck(prof_course,'course_name');
           this.prof_list = []
           /*this.assgn_list = [{
			   name : 'abc',
			   deadline : '01-01-1998',
			   status :  'Yes'
		   }]*/
           this.assgn_list=assignment_object;
           this.filterProf = function(crs_name){
        	   crs_name = $scope.selectedCourse;
        	   //alert('Here ' + crs_name);
        	   //alert('here');
        	   var totalStuff = this.prof_course.length;
        	   //alert('len : ' + totalStuff);
        	    for ( var i = 0; i < totalStuff; i++)
        	    {
        	        //alert("ID: " + prof_course[i].course_name);
        	    	var crs = prof_course[i].course_name;
        	    	if (prof_course[i].course_name.localeCompare(crs_name)==0){
        	    		//this.prof_list = prof_course[i].prof_name.slice();
        	    		for (var j=0; j < this.prof_course[i].prof_name.length ; j++){
        	    			this.prof_list.push(prof_course[i].prof_name[j]);
        	    		}
        	    		//this.prof_list=['abc','def'];
        	    	}
        	    }
        	   
           };
           this.show_assignments = function(){
        	   //alert($scope.selectedProf + "  " + $scope.selectedCourse);
        	   /*this.assgn_list.push({
    			   'name' : 'abc',
    			   'deadline' : '01-01-1998',
    			   'status' :  'Yes'
    		   });*/
        	   this.assgn_list=[];
        	   var len=assignment_object.length;
        	   //alert(len);
        	   for (var i=0;i<len;i++){
        		   if ((assignment_object[i].course_name.localeCompare($scope.selectedCourse)==0) && (assignment_object[i].prof_name.localeCompare($scope.selectedProf)==0)){
        			   this.assgn_list.push(
        					   {
        						   name : assignment_object[i].name,
        						   deadline : assignment_object[i].deadline,
        						   status :  assignment_object[i].status,
        						   assign_id : assignment_object[i].assign_id,
        						   course_name : assignment_object[i].course_name,
        						   prof_name : assignment_object[i].prof_name
        					   }
        					   );		   
        		   }
        	   }
           }
    });

})()