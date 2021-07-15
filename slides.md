---
author: Eberhard Hansis, CTO & Founder @ [Vebeto GmbH](https://www.vebeto.de)
title: GeoMob MUC
subtitle: Scripted, testable, scalable, and free!<br>A tour of geodata analysis in Python.
date: July 15, 2021
---

# Today's menu

* Vector data ➙ [geopandas](https://geopandas.org/)
* Raster data ➙ [xarray](http://xarray.pydata.org)
* (Scaling/parallelization ➙ [dask](https://dask.org))
* Data analysis Best Practices

---

# Demo time!

---

# Scaling

* [xarray + dask](http://xarray.pydata.org/en/stable/user-guide/dask.html)
  - parallel computing (one or multiple datasets!)
  - execution pipelines  
  - larger-than-memory datasets  
  - supports compute clusters
* [geopandas + dask](https://github.com/geopandas/dask-geopandas)
  - same benefits...
  - experimental!
  
---

# Best practices

for serious projects (scientific publications, business decisions, products ...)

---

# 🧨🪤🐁

---

## If you want to be a data analysis professional...

* No manual editing of input data
* No interactive data analysis  
* Fully scripted processing 
* Re-process at the push of a button

---

## Why?

* You *will* run the analysis more than once.
* You *will* run similar analyses in the future.
* You *will not* remember what you did, a year from now.
* You *will not* write good documentation.
* Automated testing becomes possible

---
  
## Other people propagating similar ideas:

- [Human Rights Data Analysis Group (HRDAG)](https://hrdag.org/2016/06/14/the-task-is-a-quantum-of-workflow/)
- [Richard McElreath, MPI EVA](https://www.youtube.com/watch?v=zwRdO9_GGhY)

---

# Version control

This demo is on [GitHub](https://github.com/ehansis/geodemo2021).

Git is a version control system.

---

### Version control gives you...

* versioned code 🤦‍
* diffing
* merging
* true collaborative work

... this rules out P💥werBI, T🦄bleau, ArcG📍s projects, Jupyter Notebooks!


---

## First law of analytics tools

> If you can easily merge changes from multiple coworkers *and* implement automated tests, you can use it.

---

# Test, Test, Test

---

## Three levels of testing

* `assert` statements
* unit tests
* consistency checks

[➮ read more](https://github.com/ehansis/til/blob/master/pages/three_levels_analytics_testing.md)

---

# Demo time!

(maybe)

---

# Happy coding!

Code, slides, etc: 

[https://github.com/ehansis/geodemo2021](https://github.com/ehansis/geodemo2021)

Eberhard Hansis, CTO & Founder @ [Vebeto GmbH](https://www.vebeto.de)

(I'm on [LinkedIn](https://www.linkedin.com/in/eberhard-hansis-95a1b833/))