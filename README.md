

## PIZZA DELIVERY API


## ROUTES TO IMPLEMENT
| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *POST* | ```/api/signup/``` | _Register new user_| _All users_|
| *POST* | ```/api/login/``` | _Login user_|_All users_|
| *POST* | ```/api/order/``` | _Place an order_|_All users_|
| *PUT* | ```/api/order/update/{order_id}/``` | _Update an order_|_All users_|
| *PUT* | ```/api/order/status/{order_id}/``` | _Update order status_|_Superuser_|
| *DELETE* | ```/api/order/delete/{order_id}/``` | _Delete/Remove an order_ |_All users_|
| *GET* | ```/api/user/orders/``` | _Get user's orders_|_All users_|
| *GET* | ```/api/orders/``` | _List all orders made_|_Superuser_|
| *GET* | ```/api/orders/{order_id}/``` | _Retrieve an order_|_Superuser_|
| *GET* | ```/api/user/order/{order_id}/``` | _Get user's specific order_|
| *GET* | ```/docs/``` | _View API documentation_|_All users_|
