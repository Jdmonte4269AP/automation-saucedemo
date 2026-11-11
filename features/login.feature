Feature: Inicio de sesion
    Background:
        Given que el usuario se encuentre en la pagina del login

    Scenario: Inicio de sesion exitoso
        When ingresa en los campos de datos "standard_user" y "secret_sauce"
        And hace click en el boton de login
        Then deberia ingresar al inventario

    Scenario: Login invalido con contraseña incorrecta
        When ingresa en los campos de datos "standard_user" y "1234"
        And hace click en el boton de login
        Then deberia mostrase el mensaje de error "Epic sadface"

    Scenario Outline: Login invalido con diferentes credenciales
        When ingresa en los campos de datos "<usuario>" y "<password>"
        And hace click en el boton de login
        Then deberia mostrase el mensaje de error "<mensaje>"

        Examples:
            |usuario|password|mensaje|
            |standard_user|1234|Epic sadface: Username and password do not match any user in this service|
            |standart_user|secret_sauce|Epic sadface: Username and password do not match any user in this service|
            |VACIO|secret_sauce|Epic sadface: Username is required|
            |standard_user|VACIO|Epic sadface: Password is required|
    
