var kalpavrukshApp = angular.module("infinitylabsApp", [
	'ui-notification',
    'angular-loading-bar',
]);

kalpavrukshApp.config(['NotificationProvider', '$httpProvider', function(NotificationProvider, $httpProvider) {

    NotificationProvider.setOptions({
        delay: 3000,
        startTop: 20,
        startRight: 10,
        verticalSpacing: 20,
        horizontalSpacing: 20,
        positionX: 'right',
        positionY: 'top'
    });

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

}]);

kalpavrukshApp.controller("infinitylabsControllers", ['$scope', '$log', '$http','$timeout', function($scope, $log, $http, $timeout) {
	console.log("infinitylabsControllers loads");

	

}]);