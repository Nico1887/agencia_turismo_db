# Agencia de Turismo – Base de Datos Relacional

## 📌 Descripción
Sistema de base de datos para la gestión de una agencia de turismo.
Permite administrar clientes, paquetes turísticos, reservas, seguros,
transportes y destinos, garantizando integridad y normalización hasta 3NF.

## 🧱 Modelo de Datos
- Normalización hasta Tercera Forma Normal (3NF)
- Relaciones N:N resueltas mediante tablas intermedias
- Integridad referencial mediante claves foráneas
- Validaciones con CHECK constraints

## ⚙️ Funcionalidades
- Alta y baja lógica de clientes
- Reserva de paquetes con control de cupo
- Gestión de seguros y transportes
- Stored Procedures para lógica de negocio
- Índices para optimización de consultas

## 🛠️ Tecnologías
- SQL Server (T-SQL)

## 📊 Diagrama ER
El DER refleja la estructura lógica del sistema, incluyendo clientes, reservas, paquetes turísticos, destinos, transportes, seguros y métodos de pago.

![Diagrama DER](docs/diagrama_bd_agencia_turismo.png)

## 🚀 Próximos pasos
- API REST
- Frontend web
- Autenticación de usuarios



