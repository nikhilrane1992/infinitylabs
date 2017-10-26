var infinitylabsApp = angular.module("infinitylabsApp", [
    'ui-notification',
    'angular-loading-bar',
]);

infinitylabsApp.config(['NotificationProvider', '$httpProvider', function(NotificationProvider, $httpProvider) {

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


infinitylabsApp.controller("infinitylabsControllers", ['$scope', '$log', '$http', '$timeout', 'Notification', function($scope, $log, $http, $timeout, Notification) {
    console.log("infinitylabsControllers loads");
    $http.defaults.headers.common.Authorization = localStorage.getItem('infinitylabs.token');
    var routerDetails = function() {
        $http.get('/router_details/').
        success(function(data, status, headers, config) {
            if (data.status) {
                $scope.routerDetails = data.data;
            } else {
                Notification.error(data.validation)
                window.location = data.redirect_url;
            }
        }).
        error(function(data, status, headers, config) {
            Notification.error(data)
        });
    }

    $scope.routerDetailsObj = {
        loopback: "",
        hostname: "",
        brand: "",
        item_height: "",
        item_weight: "",
        dimensions: "",
        model_number: "",
        router_type: "",
        id: null
    }
    $scope.saveRouterDetails = function() {
        $http.post('/save/router/details/', $scope.routerDetailsObj).
        success(function(data, status, headers, config) {
            if (data.status) {
                Notification.success(data.validation);
            } else {
                Notification.error(data.validation)
            }
        }).
        error(function(data, status, headers, config) {
            Notification.error("Login invalid")
        });
    }
    $scope.updateRouterDetails = function(routerObj) {
        $scope.routerDetailsObj = routerObj;
    }



    routerDetails();
}]);

infinitylabsApp.controller("loginControllers", ['$scope', '$log', '$http', '$timeout', 'Notification', function($scope, $log, $http, $timeout, Notification) {
    console.log("loginControllers loads");
    $scope.username = "";
    $scope.password = "";
    $scope.login = function() {
        $http.post('/auth_view/', { username: $scope.username, password: $scope.password }).
        success(function(data, status, headers, config) {
            if (data.status) {
                localStorage.setItem('infinitylabs.token', data.token);
                $http.defaults.headers.common.Authorization = data.token
                window.location = /home/;
            } else {
                Notification.error(data.validation)
            }
        }).
        error(function(data, status, headers, config) {
            Notification.error("Login invalid")
        });
    }

}]);