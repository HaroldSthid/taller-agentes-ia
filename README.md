# Taller: los lunes empiezan de cero

**Agentes de IA para que la información no se pierda entre áreas.**

Una operación se rompe casi siempre en el mismo sitio: cuando la información pasa de un área a otra. Ventas promete algo, Logística no se entera, Servicio al Cliente recibe el reclamo y nadie recuerda qué pasó la semana pasada. En este taller ves cómo un equipo de agentes de IA hace lo que hoy hacemos mal con prisa: **pasar el contexto completo de un área a la siguiente y dejar memoria de lo que ocurrió.**

Primero lo ves en un caso cercano (la rutina diaria de una familia). Después lo llevas a un traspaso de tu empresa.

> Todo el material usa datos ficticios. Mientras pruebas, no pegues nombres ni datos reales de clientes.

---

## Elige tu ruta

| Si tú... | Haz esto |
| --- | --- |
| **Solo quieres entender la idea** | Mira la [presentación](https://haroldsthid.github.io/taller-agentes-ia/) y la demo. No necesitas instalar nada |
| **No programas, pero quieres llevarlo a tu empresa** | Llena la hoja de trabajo y entrégasela, con el prompt, a una IA de código que escribe el prototipo por ti |
| **Sabes usar un repositorio de GitHub** | Sigue la guía de 30 minutos: copias una plantilla, editas un solo archivo y lo corres |

El código y las guías viven en otro repositorio, para que haya una sola versión de todo:
**[HaroldSthid/GeminiADKPracticeCOL](https://github.com/HaroldSthid/GeminiADKPracticeCOL)**, fijado a la etiqueta `taller-v1.1`.

| Material | Dónde está |
| --- | --- |
| Hoja de trabajo del reto (para imprimir) | [`workshop/RETO_OPCION_A.md`](https://github.com/HaroldSthid/GeminiADKPracticeCOL/blob/taller-v1.1/workshop/RETO_OPCION_A.md) |
| Guion del taller | [`workshop/NARRATIVA.md`](https://github.com/HaroldSthid/GeminiADKPracticeCOL/blob/taller-v1.1/workshop/NARRATIVA.md) |
| Guía técnica: adáptalo a tu empresa en 30 minutos | [`workshop/ADAPTA_A_TU_EMPRESA.md`](https://github.com/HaroldSthid/GeminiADKPracticeCOL/blob/taller-v1.1/workshop/ADAPTA_A_TU_EMPRESA.md) |
| Prompt para una IA de código | [`workshop/PROMPT_PARA_IA_DE_CODIGO.md`](https://github.com/HaroldSthid/GeminiADKPracticeCOL/blob/taller-v1.1/workshop/PROMPT_PARA_IA_DE_CODIGO.md) |

---

## Antes de llegar (15 minutos)

Si vas a probarlo en tu computador, déjalo listo antes del taller. Con la red del evento compartida, instalar ahí es lento.

1. **Python 3.10 o superior.** Compruébalo con `python --version`.
2. **Una clave gratuita de Google AI Studio:** <https://aistudio.google.com/app/apikey>. Cada persona usa la suya. No la compartas por chat ni la subas a ningún repositorio.
3. **Clona el código en una carpeta de ruta corta.** En Windows, por ejemplo `C:\taller`. Las dependencias de Google traen archivos con nombres larguísimos y, en una carpeta muy anidada, la instalación falla con `WinError 206`.

```bash
git clone --branch taller-v1.1 --depth 1 https://github.com/HaroldSthid/GeminiADKPracticeCOL.git
cd GeminiADKPracticeCOL/adk-web
python -m venv .venv
```

Al terminar el `git clone`, git imprime un aviso largo que dice que estás en estado **"detached HEAD"**. **Es normal y puedes ignorarlo**: aparece siempre que se clona una versión fija (una etiqueta) y no un error. No tienes que hacer nada.

4. **Instala y prueba**, siguiendo "Antes de empezar" de la [guía técnica](https://github.com/HaroldSthid/GeminiADKPracticeCOL/blob/taller-v1.1/workshop/ADAPTA_A_TU_EMPRESA.md). Ahí está explicado qué hacer en Windows si PowerShell bloquea la activación del entorno. Si `pytest` pasa, estás listo.

¿No pudiste instalarlo? No pasa nada: el notebook de Colab del repositorio corre en el navegador, sin instalar nada.

---

## Lo que te llevas

1. Un agente es un **modelo**, unas **reglas**, unas **herramientas** y una **memoria**.
2. El valor no está en que la IA sea más lista, sino en el **traspaso de contexto** entre áreas.
3. Sin una **bitácora compartida**, cada día empieza de cero.
4. Un prototipo que corre, o una hoja de trabajo lista para que otra persona lo construya.

## Lo que esto es y lo que no es

- **Es** una forma de probar si un traspaso de tu empresa se puede ordenar con agentes y una bitácora compartida.
- **No es** una integración con tus sistemas (ERP, CRM). Conectarlo es un proyecto con el equipo de TI.
- **No decide por ti.** Los agentes proponen y registran. Las decisiones críticas siguen siendo de una persona.
- **No reemplaza revisar.** El modelo puede rellenar con frases agradables. Contrasta siempre su análisis con la bitácora.

---

## Para quien presenta

La presentación es un solo archivo, `index.html`, sin instalar nada. En una pantalla horizontal se presenta diapositiva por diapositiva; en un teléfono se lee como una página que baja. Para abrirla en local, basta con abrir el archivo en el navegador.

| Tecla | Qué hace |
| --- | --- |
| `←` `→` o espacio | Cambia de diapositiva |
| `N` | Muestra u oculta las notas del orador |
| `F` | Pantalla completa |
| `T` | Cambia entre tema claro y oscuro |
| `A` | Reproduce o pausa el audio de la diapositiva actual |
| `B` | Salta al índice del bonus track |
| `1` `2` `3` | En el índice del bonus track, salta al bloque elegido |

Las diapositivas 1 a 22 son el taller. De la 23 en adelante está el **bonus track**: material de apoyo para las preguntas que suelen surgir (cuándo usar un agente, cuánto cuesta, qué otros patrones de diseño hay). No se presenta en orden: se abre solo si alguien pregunta.

### Audio de apoyo

Cada diapositiva con explicación (1 a 21) y cada bloque del bonus track (24, 25 y 29) tiene un clip de audio de 10 a 50 segundos. En un teléfono aparece un botón **Escuchar** con la duración y un enlace **Transcripción**; al presentar en pantalla horizontal los botones se ocultan y la tecla `A` reproduce el clip. Es una **voz sintética** (generada con Artlist, voz Norah, español latino) y el texto de cada clip es el de su transcripción. Los 24 archivos MP3 están en `assets/audio/` (unos 6 MB en total) y solo se descargan cuando alguien pulsa el botón.

Si cambias el texto de una diapositiva, la transcripción y el audio quedan desactualizados: edita la transcripción en `index.html` y vuelve a generar el clip con el mismo nombre de archivo (`s05.mp3` para la diapositiva 5, `b25.mp3` para el bloque de costos).

El código QR de la diapositiva «Material» (la 22) apunta a `https://haroldsthid.github.io/taller-agentes-ia/`. Si cambias el nombre del repositorio o el usuario, regéneralo con `python tools/make_qr.py <nueva-direccion>` (necesita `pip install segno`) y haz commit del archivo `assets/qr-presentacion.svg`.

## Licencia

MIT. Puedes usar, copiar y adaptar este material, incluida la presentación. Los detalles están en [`LICENSE`](LICENSE).
