import sys as xalif,asyncio as xalif_async,inspect as xalif_inspect
from pathlib import Path as xalif_path
xalif.path.insert(0,str(xalif_path(__file__).resolve().parent))
import secenddata as xalif_core
xalif_main=getattr(xalif_core,"main",None)
if not callable(xalif_main):raise SystemExit("XALIF ERROR")
xalif_result=xalif_main()
if xalif_inspect.isawaitable(xalif_result):xalif_async.run(xalif_result)