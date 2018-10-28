# Stubs for pyspark.ml.util (Python 3.5)
#

from typing import Any, Optional
from pyspark.sql.context import SQLContext
from pyspark.sql.session import SparkSession

basestring = ...  # type: type
unicode = ...  # type: type

class Identifiable:
    uid = ...  # type: str
    def __init__(self) -> None: ...

class BaseReadWrite:
    def __init__(self) -> None: ...
    def context(self, sqlContext: Any) -> None: ...
    def session(self, sparkSession: Any): ...
    @property
    def sparkSession(self): ...
    @property
    def sc(self): ...

class MLWriter(BaseReadWrite):
    shouldOverwrite: bool = ...
    def __init__(self) -> None: ...
    def save(self, path: str) -> None: ...
    def saveImpl(self, path: str) -> None: ...    
    def overwrite(self) -> MLWriter: ...

class JavaMLWriter(MLWriter):
    def __init__(self, instance) -> None: ...
    def save(self, path: str) -> None: ...
    def overwrite(self) -> JavaMLWriter: ...
    def context(self, sqlContext: SQLContext) -> JavaMLWriter: ...
    def session(self, sparkSession: SparkSession) -> JavaMLWriter: ...

class MLWritable:
    def write(self) -> MLWriter: ...
    def save(self, path: str) -> None: ...

class JavaMLWritable(MLWritable):
    def write(self) -> JavaMLWriter: ...

class MLReader:
    def load(self, path: str) -> Any: ...
    def context(self, sqlContext: SQLContext) -> MLReader: ...
    def session(self, sparkSession: SparkSession) -> MLReader: ...

class JavaMLReader(MLReader):
    def __init__(self, clazz: type) -> None: ...
    def load(self, path: str) -> Any: ...
    def context(self, sqlContext: SQLContext) -> JavaMLReader: ...
    def session(self, sparkSession: SparkSession) -> JavaMLReader: ...

class MLReadable:
    @classmethod
    def read(cls) -> MLReader: ...
    @classmethod
    def load(cls, path: str) -> MLReadable: ...

class JavaMLReadable(MLReadable):
    @classmethod
    def read(cls) ->  JavaMLReader: ...

class JavaPredictionModel:
    @property
    def numFeatures(self) -> int: ...

class DefaultParamsWritable(MLWritable):
    def write(self): ...

class DefaultParamsWriter(MLWriter):
    instance: Any = ...
    def __init__(self, instance: Any) -> None: ...
    def saveImpl(self, path: Any) -> None: ...
    @staticmethod
    def saveMetadata(instance: Any, path: Any, sc: Any, extraMetadata: Optional[Any] = ..., paramMap: Optional[Any] = ...) -> None: ...

class DefaultParamsReadable(MLReadable):
    @classmethod
    def read(cls): ...

class DefaultParamsReader(MLReader):
    cls: Any = ...
    def __init__(self, cls: Any) -> None: ...
    def load(self, path: Any): ...
    @staticmethod
    def loadMetadata(path: Any, sc: Any, expectedClassName: str = ...): ...
    @staticmethod
    def getAndSetParams(instance: Any, metadata: Any) -> None: ...
    @staticmethod
    def loadParamsInstance(path: Any, sc: Any): ...
