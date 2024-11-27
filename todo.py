import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Título de la app
st.title("EJERCICIOS RESUELTOS ")

# Análisis de la función f(x) = x^2 - 4x + 5
st.subheader("EJERCICIO 1.Análisis de la función f(x) = x^2 - 4x + 5")

st.write("""
La función \(f(x) = x^2 - 4x + 5\) es una parábola que abre hacia arriba. Vamos a analizar sus puntos críticos y su mínimo global.
""")

def f1(x):
    return x**2 - 4*x + 5

def f_prime1(x):
    return 2*x - 4

def f_double_prime1(x):
    return 2

# Resolución del problema
st.subheader("Resolución detallada del problema")

# Paso 1: Calcular la derivada y puntos críticos
st.markdown("**Paso 1: Calcular la derivada y encontrar los puntos críticos**")
critical_point = 2  # f'(x) = 0 -> 2x - 4 = 0 -> x = 2
st.latex(r"f'(x) = 2x - 4 \quad \implies \quad f'(x) = 0 \quad \implies \quad x = 2")

# Paso 2: Evaluar la segunda derivada
st.markdown("**Paso 2: Evaluar la segunda derivada en el punto crítico**")
second_derivative = f_double_prime1(critical_point)
if second_derivative > 0:
    st.latex(r"f''(x) = 2 > 0 \quad \implies \quad x = 2 \text{ es un mínimo local.}")
else:
    st.latex(r"f''(x) = 2 \leq 0 \quad \implies \quad x = 2 \text{ no es un mínimo.}")

# Paso 3: Analizar el comportamiento global
st.markdown("**Paso 3: Analizar el comportamiento global**")
st.markdown("La función \(f(x) = x^2 - 4x + 5\) es una parábola con coeficiente principal positivo (\(x^2\)), por lo que abre hacia arriba. Esto implica que tiene un único mínimo global en \(x = 2\).")

# Paso 4: Verificar en los puntos \(x = 2\) y \(x = 0\)
st.markdown("**Paso 4: Evaluar en los puntos dados**")
x_values = [2, 0]
results = []
for x in x_values:
    value = f1(x)
    if x == critical_point:
        results.append((x, value, "Mínimo Local y Global"))
    else:
        results.append((x, value, "No es mínimo local ni global"))

# Mostrar resultados en una tabla
st.markdown("**Resultados de la evaluación:**")
st.write(
    """
    | Punto \(x\) | Valor \(f(x)\) | Clasificación |
    |-------------|---------------|----------------|
    | \(x = 2\)   | \(f(2) = 1\)  | Mínimo Local y Global |
    | \(x = 0\)   | \(f(0) = 5\)  | No es mínimo local ni global |
    """
)

# Gráfica de la función
st.subheader("Gráfica de la función")
x = np.linspace(-2, 6, 500)
y = f1(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r"$f(x) = x^2 - 4x + 5$", linewidth=2)
plt.scatter([2], [f1(2)], color="red", label="Mínimo Global (x=2)", zorder=5, s=100)
plt.scatter([0], [f1(0)], color="blue", label="Evaluación (x=0)", zorder=5, s=100)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.title("Gráfica de la función \(f(x) = x^2 - 4x + 5\)", fontsize=16)
plt.xlabel("x", fontsize=12)
plt.ylabel("f(x)", fontsize=12)
plt.legend(fontsize=10)
plt.grid(alpha=0.5)
plt.tight_layout()

st.pyplot(plt)

# Explicación final
st.subheader("Conclusión")
st.write("""
1. El punto \(x = 2\) es un **mínimo local** porque cumple las condiciones en un vecindario, y también es un **mínimo global** porque es el punto de menor valor en todo el dominio.
2. El punto \(x = 0\) **no es un mínimo local ni global**, ya que no cumple con ninguna de las definiciones.
""")

# Análisis de la función f(x) = |x|
st.subheader("EJERCICIO 2. f(x) = |x|")

st.write("""
La función \(f(x) = |x|\) es una función de valor absoluto. Su gráfica tiene forma de "V", con un vértice en \(x = 0\), donde la función alcanza su valor más bajo.
""")

def f2(x):
    return np.abs(x)

# Gráfica de la función
x_values = np.linspace(-10, 10, 400)
y_values = f2(x_values)

plt.figure(figsize=(6, 4))
plt.plot(x_values, y_values, label='f(x) = |x|', color='blue')
plt.scatter(0, 0, color='red', zorder=5, label="Mínimo global en x=0")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("Gráfica de la función f(x) = |x|")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

st.pyplot(plt)

st.write("""
### Conclusión:
- En \(x = 0\), la función \(f(x) = |x|\) alcanza su valor más bajo, que es \(f(0) = 0\), y para cualquier \(x \neq 0\), \(f(x) > 0\).
- Esto implica que \(x = 0\) es un **mínimo global**, ya que es el valor mínimo en todo el dominio de la función.
""")

# Análisis de la función f(x) = sin(x) en [0, π]
st.subheader("EJERCICIO 3. f(x) = sin(x) en [0, π]")

st.write("""
Vamos a analizar la función \(f(x) = \sin(x)\) en el intervalo cerrado \([0, \pi]\), y cómo el Teorema de Weierstrass se aplica para asegurar que esta función tiene un mínimo global en este intervalo.
""")

def f3(x):
    return np.sin(x)

x_values = np.linspace(0, np.pi, 400)
y_values = f3(x_values)

plt.figure(figsize=(6, 4))
plt.plot(x_values, y_values, label='f(x) = sin(x)', color='blue')
plt.scatter(0, 0, color='red', zorder=5, label="Mínimo global en x=0")
plt.scatter(np.pi, 0, color='red', zorder=5, label="Mínimo global en x=π")
plt.scatter(np.pi/2, 1, color='green', zorder=5, label="Máximo global en x=π/2")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("Gráfica de la función f(x) = sin(x) en el intervalo [0, π]")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

st.pyplot(plt)

st.write("""
### Conclusión:
- El **mínimo global** de \(f(x) = \sin(x)\) en \([0, \pi]\) es 0, alcanzado en \(x = 0\) y \(x = \pi\).
- El **máximo global** es 1, alcanzado en \(x = \pi/2\).
""")

# Análisis de la función f(x, y) = x^2 + y^2 con restricción x^2 + y^2 ≤ 1
st.subheader("EJERCICIO 4. f(x, y) = x^2 + y^2 con restricción x^2 + y^2 ≤ 1")

st.write("""
La función \(f(x, y) = x^2 + y^2\) está sujeta a la restricción \(x^2 + y^2 \leq 1\), que describe un círculo de radio 1 centrado en el origen.
""")

def f4(x, y):
    return x**2 + y**2

# Crear una malla de puntos (x, y)
x = np.linspace(-1, 1, 400)
y = np.linspace(-1, 1, 400)
X, Y = np.meshgrid(x, y)

# Definir la función f(x, y) = x^2 + y^2
Z = X**2 + Y**2

# Crear la gráfica de la función
plt.figure(figsize=(6, 6))
cp = plt.contourf(X, Y, Z, 20, cmap='viridis')
plt.colorbar(cp, label='f(x, y) = x^2 + y^2')

# Marcamos el mínimo global en el origen
plt.scatter(0, 0, color='red', zorder=5, label="Mínimo global en (0, 0)")

# Añadir etiquetas y leyenda
plt.title("Gráfica de f(x, y) = x^2 + y^2 con restricción x^2 + y^2 ≤ 1")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

st.pyplot(plt)

st.write("""
### Conclusión:
El **mínimo global** de la función \(f(x, y) = x^2 + y^2\) en el dominio \(x^2 + y^2 \leq 1\) se encuentra en \((0, 0)\), donde \(f(0, 0) = 0\).
""")

# Análisis de la función f(x) = x^4 - 4x^2 + 4 (Mínimo Global No Único)
st.subheader("EJERCICIO 5. Ejemplo de Mínimo Global No Único")

st.write("""
Consideremos la función \(f(x) = x^4 - 4x^2 + 4\). Esta función tiene dos puntos donde alcanza su valor mínimo global, lo que demuestra que el mínimo global **no es único**.
""")

def f5(x):
    return x**4 - 4*x**2 + 4

x = np.linspace(-3, 3, 400)
y = f5(x)

plt.figure(figsize=(6, 6))
plt.plot(x, y, label="f(x) = x^4 - 4x^2 + 4", color='blue')

# Marcamos los puntos de mínimo global
plt.scatter(np.sqrt(2), f5(np.sqrt(2)), color='red', zorder=5, label="Mínimo global en x = √2")
plt.scatter(-np.sqrt(2), f5(-np.sqrt(2)), color='red', zorder=5, label="Mínimo global en x = -√2")

# Añadir etiquetas y leyenda
plt.title("Gráfica de f(x) = x^4 - 4x^2 + 4")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

st.pyplot(plt)

st.write("""
### Conclusión:
La función tiene dos puntos donde alcanza su valor mínimo global, en \(x = \sqrt{2}\) y \(x = -\sqrt{2}\), lo que demuestra que el mínimo global no es único.
""")
