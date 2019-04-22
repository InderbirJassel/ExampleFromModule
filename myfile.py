+import matplotlib
+import numpy as np

 from matplotlib import pylab
 from matplotlib.backends.backend_pdf import PdfPages

+def increment_or_add(key,hash,weight=1):
+       if key not in hash:
+               hash[key]=0
+       hash[key]+=weight
+
 data_path=os.path.join(os.path.dirname(
                        os.path.abspath(__file__)),
-regenerate=False
+regenerate=True