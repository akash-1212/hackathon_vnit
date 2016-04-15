(function(){
	var app = angular.module('store', [ ]);
	app.controller('StoreController',function($scope){
		this.cart = cart_items;
		this.cart_map = cart_map;
		this.totalval=0;
		$scope.getTotal = function(){
			this.cart_map = cart_map
			var total=0;
			for(var m in cart_map){
				total = total + cart_map[m].item_quantity*cart_map[m].item_rate;
			}
//			console.log("total  " +  total);
//			$.each(cart_map, function(key, value) {
//			    alert(key + " " + value.item_name + " " + value.item_quantity);
//			});
			totalval=total;
			return total;
		};
	});
	
	app.controller('SendJSONController',function(){
		this.sendObject = function(){
//		alert('Hello world');
//			$.each(cart_map, function(key, value) {
//		    alert(key + " " + value.item_name + " " + value.item_quantity);
//		});
		$.each(cart_map,function(key,value){
			cart_items.push({
				item_code : key,
				item_name : value.item_name,
				item_rate : value.item_rate,
				item_quantity : value.item_quantity
			})
		});
		var data1 = JSON.stringify({data:cart_items});
		console.log(data1);
		//alert('hello1');
		$.ajax({
		    url: "harshada",
		    data: data1,
		    dataType: 'json',
		    contentType: 'application/json',
		    type: 'POST',
		    async: true,
		    success: function (res) {
//		        console.log(res.data.length);
//		        for (var i = 0; i < res.data.length; i++) {
//		            console.log(" " + res.data[i].item_code + "-" + res.data[i].item_name + "-" + res.data[i].item_rate + "-    " + res.data[i].item_quantity);
//		        }
				document.submitform.action="payment";
				document.submitform.submit();
		    },
			error:function(XMLHttpRequest, textStatus, errorThrown){
				//alert('Error ' + textStatus);
		        //alert(errorThrown);
			}
		});
		};
	});
	
	 app.filter('sumFilter', function() {
	     return function(cart_map) {
	         var total=0;
				for(var m in cart_map){
					total = total + cart_maps[m].item_quantity*cart_map[m].item_rate;
				}
				alert(total);
	         return total;
	     };
	 });
	
//	app.controller('CartController', ['$scope', function($scope) {
//		   scope.addToCart = function() {
//			   alert('Here');
//			   cart_items.push({
//					item_code : $scope.icode,
//					item_name : $scope.iname,
//					item_rate : $scope.icost
//				}); 
//		   };
//	}]);
	
	app.controller('CartController',function(){
		this.cart_mappy = cart_map;
		this.cart = cart_items;
		this.addToCart = function(code,name,rate){
		this.code=code;
		this.name=name;
		this.rate=rate;
		this.Total=0;
//		cart_items.push({
//			item_code : this.code,
//			item_name : this.name,
//			item_rate : this.rate
//		});
		if (cart_map[this.code] === undefined){
			cart_map[this.code] = {
					  item_name : name,
			      	  item_rate : rate,
			      	  item_quantity : 1
				};
		}
		else{
			var q = cart_map[this.code].item_quantity;
			cart_map[this.code] = {
					  item_name : name,
			      	  item_rate : rate,
			      	  item_quantity : q+1
				};
		}
//		$.each(cart_map, function(key, value) {
//		    alert(key + " " + value.item_name + " " + value.item_quantity);
//		});
		};
		
		
		this.removeFromCart = function(code,name,rate){
			this.code=code;
			this.name=name;
			this.rate=rate;
			this.Total=0;
			if (cart_map[this.code] === undefined){
				console.log("Empty field -1");
			}
			else{
				var q = cart_map[this.code].item_quantity;
				if (q>1){
				cart_map[this.code] = {
						  item_name : name,
				      	  item_rate : rate,
				      	  item_quantity : q-1
					};
				}
				else{
					delete cart_map[this.code];
				}
			}
//			$.each(cart_map, function(key, value) {
//			    alert(key + " " + value.item_name + " " + value.item_quantity);
//			});
			};
		
		
		
		
		
		
	});
	
	var cart_items = [];
	
	var cart_map = {};
//	cart_map["BLAH"] = {
//		  item_name : "Codechef",
//      	  item_rate : "3.40",
//      	  item_quantity : 2
//	};

})()