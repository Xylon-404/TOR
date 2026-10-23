
import sys as xalif
import asyncio as xalif_async
import inspect as xalif_inspect
from pathlib import Path as xalif_path

xalif.path.insert(
    0,
    str(xalif_path(__file__).resolve().parent)
)

import protected_core as xalif_core

xalif_main = getattr(xalif_core, "main", None)

if not callable(xalif_main):
    raise SystemExit(
        "XALIF ERROR: main() function not found in protected_core"
    )

xalif_result = xalif_main()

if xalif_inspect.isawaitable(xalif_result):
    xalif_async.run(xalif_result)
