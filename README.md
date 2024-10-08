
# Descripción de Archivos

Este repositorio contiene varios archivos que abordan diferentes aspectos de sistemas operativos y programación. A continuación, se proporciona una descripción detallada de cada archivo.

## Archivos C
1. **board_.c**: 
   Este archivo probablemente esté relacionado con la configuración o el manejo de la placa base (motherboard) en un sistema informático. Contiene funciones que interactúan con los componentes del hardware a bajo nivel, posiblemente para la gestión de la comunicación interna entre diferentes partes del sistema.

2. **disco_duro_.c**: 
   Enfocado en la gestión y control del disco duro, este archivo contiene funciones para realizar operaciones básicas como la lectura y escritura de datos, la manipulación de sectores y el acceso a la memoria de almacenamiento del disco duro. Es fundamental para manejar cómo el sistema operativo interactúa con el almacenamiento físico.

3. **memoria_.c**: 
   Dedicado a la administración de la memoria en sistemas operativos, este archivo incluye funciones para la asignación y liberación de memoria, gestión de la memoria dinámica y técnicas para optimizar el uso de la memoria física del sistema. Puede también involucrar el manejo de la memoria virtual para procesos en ejecución.

4. **Memory_.c**: 
   Aunque también trata sobre la memoria del sistema, este archivo puede abordar aspectos específicos o implementar funciones diferentes en comparación con `memoria_.c`. Es posible que esté optimizado para otro tipo de arquitectura o que implemente técnicas avanzadas de gestión de memoria para mejorar el rendimiento.

5. **periferico_.c**: 
   Este archivo se enfoca en la interacción y control de dispositivos periféricos, tales como teclados, ratones, impresoras y otros dispositivos de entrada/salida. Implementa funciones que permiten la comunicación fluida entre el sistema operativo y los dispositivos externos conectados.

6. **SO_info_.c**: 
   Contiene funciones para recopilar y mostrar información relevante sobre el sistema operativo en el que se está ejecutando. Esto puede incluir detalles sobre el núcleo del sistema, la versión del sistema operativo, el estado actual del sistema y otros datos útiles para el diagnóstico y análisis de rendimiento.

## Archivos Python
1. **facto_i.py**: 
   Un programa en Python que calcula el factorial de un número utilizando un enfoque iterativo. Este método es eficiente en términos de uso de memoria, ya que no requiere almacenar múltiples llamados en la pila de ejecución, lo que lo hace adecuado para cálculos con números grandes.

2. **facto_r.py**: 
   Un programa en Python que calcula el factorial de un número mediante un enfoque recursivo. Aunque este método es más intuitivo y fácil de implementar, su consumo de memoria puede ser alto para números grandes debido al uso de la pila de llamadas, lo que puede llevar a una mayor complejidad en el manejo del espacio.
