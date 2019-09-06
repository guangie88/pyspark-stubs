# Stubs for pyspark.ml.regression (Python 3.5)
#

from typing import Any, List, Optional, Sequence, TypeVar
from pyspark.ml.param.shared import *
from pyspark.ml.linalg import Vector
from pyspark.ml.util import *
from pyspark.ml.wrapper import JavaEstimator, JavaModel, JavaWrapper
from pyspark.sql.dataframe import DataFrame

P = TypeVar("P")

class LinearRegression(JavaEstimator[LinearRegressionModel], HasFeaturesCol, HasLabelCol, HasPredictionCol, HasMaxIter, HasRegParam, HasTol, HasElasticNetParam, HasFitIntercept, HasStandardization, HasSolver, HasWeightCol, HasAggregationDepth, JavaMLWritable, JavaMLReadable[LinearRegression]):
    def __init__(self, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., maxIter: int = ..., regParam: float = ..., elasticNetParam: float = ..., tol: float = ..., fitIntercept: bool = ..., standardization: bool = ..., solver: str = ..., weightCol: Optional[str] = ..., aggregationDepth: int = ...) -> None: ...
    def setParams(self, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., maxIter: int = ..., regParam: float = ..., elasticNetParam: float = ..., tol: float = ..., fitIntercept: bool = ..., standardization: bool = ..., solver: str = ..., weightCol: Optional[str] = ..., aggregationDepth: int = ...) -> LinearRegression: ...

class LinearRegressionModel(JavaModel, JavaPredictionModel, GeneralJavaMLWritable, JavaMLReadable[LinearRegressionModel], HasTrainingSummary[LinearRegressionSummary]):
    @property
    def coefficients(self) -> Vector: ...
    @property
    def intercept(self) -> float: ...
    @property
    def summary(self) -> LinearRegressionSummary: ...
    @property
    def hasSummary(self) -> bool: ...
    def evaluate(self, dataset: DataFrame) -> LinearRegressionSummary: ...

class LinearRegressionSummary(JavaWrapper):
    @property
    def predictions(self) -> DataFrame: ...
    @property
    def predictionCol(self) -> str: ...
    @property
    def labelCol(self) -> str: ...
    @property
    def featuresCol(self) -> str: ...
    @property
    def explainedVariance(self) -> float: ...
    @property
    def meanAbsoluteError(self) -> float: ...
    @property
    def meanSquaredError(self) -> float: ...
    @property
    def rootMeanSquaredError(self) -> float: ...
    @property
    def r2(self) -> float: ...
    @property
    def r2adj(self) -> float: ...
    @property
    def residuals(self) -> DataFrame: ...
    @property
    def numInstances(self) -> int: ...
    @property
    def devianceResiduals(self) -> List[float]: ...
    @property
    def coefficientStandardErrors(self) -> List[float]: ...
    @property
    def tValues(self) -> List[float]: ...
    @property
    def pValues(self) -> List[float]: ...

class LinearRegressionTrainingSummary(LinearRegressionSummary):
    @property
    def objectiveHistory(self) -> List[float]: ...
    @property
    def totalIterations(self) -> int: ...

class IsotonicRegression(JavaEstimator[IsotonicRegressionModel], HasFeaturesCol, HasLabelCol, HasPredictionCol, HasWeightCol, JavaMLWritable, JavaMLReadable[IsotonicRegression]):
    isotonic: Param
    featureIndex: Param
    def __init__(self, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., weightCol: Optional[str] = ..., isotonic: bool = ..., featureIndex: int = ...) -> None: ...
    def setParams(self, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., weightCol: Optional[str] = ..., isotonic: bool = ..., featureIndex: int = ...) -> IsotonicRegression: ...
    def setIsotonic(self, value: bool) -> IsotonicRegression: ...
    def getIsotonic(self) -> bool: ...
    def setFeatureIndex(self, value: int) -> IsotonicRegression: ...
    def getFeatureIndex(self) -> int: ...

class IsotonicRegressionModel(JavaModel, JavaMLWritable, JavaMLReadable[IsotonicRegressionModel]):
    @property
    def boundaries(self) -> Vector: ...
    @property
    def predictions(self) -> Vector: ...

class DecisionTreeParams(Params):
    maxDepth: Param
    maxBins: Param
    minInstancesPerNode: Param
    minInfoGain: Param
    maxMemoryInMB: Param
    cacheNodeIds: Param
    def __init__(self) -> None: ...
    def setMaxDepth(self: T, value: int) -> T: ...
    def getMaxDepth(self) -> int: ...
    def setMaxBins(self: T, value: int) -> T: ...
    def getMaxBins(self) -> int: ...
    def setMinInstancesPerNode(self: T, value: int) -> T: ...
    def getMinInstancesPerNode(self) -> int: ...
    def setMinInfoGain(self: T, value: float) -> T: ...
    def getMinInfoGain(self) -> float: ...
    def setMaxMemoryInMB(self: T, value: int) -> T: ...
    def getMaxMemoryInMB(self) -> int: ...
    def setCacheNodeIds(self: T, value: bool) -> T: ...
    def getCacheNodeIds(self) -> bool: ...

class TreeEnsembleParams(DecisionTreeParams):
    supportedFeatureSubsetStrategies: List[str]
    subsamplingRate: Param
    featureSubsetStrategy: Param
    def __init__(self) -> None: ...
    def getSubsamplingRate(self) -> float: ...
    def getFeatureSubsetStrategy(self) -> str: ...

class HasVarianceImpurity(Params):
    supportedImpurities: List[str]
    impurity: Param
    def __init__(self) -> None: ...
    def getImpurity(self) -> str: ...

class TreeRegressorParams(HasVarianceImpurity): ...

class RandomForestParams(TreeEnsembleParams):
    numTrees: Param
    def __init__(self) -> None: ...
    def getNumTrees(self) -> int: ...

class GBTParams(TreeEnsembleParams, HasMaxIter, HasStepSize, HasValidationIndicatorCol):
    stepSize: Param
    validationTol: Param
    def getValidationTol(self) -> float: ...

class GBTRegressorParams(GBTParams, TreeRegressorParams):
    supportedLossTypes: List[str]
    lossType: Param
    def getLossType(self) -> str: ...

class DecisionTreeRegressor(JavaEstimator[DecisionTreeRegressionModel], HasFeaturesCol, HasLabelCol, HasWeightCol, HasPredictionCol, DecisionTreeParams, TreeRegressorParams, HasCheckpointInterval, HasSeed, JavaMLWritable, JavaMLReadable[DecisionTreeRegressor], HasVarianceCol):
    def __init__(self, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., maxDepth: int = ..., maxBins: int = ..., minInstancesPerNode: int = ..., minInfoGain: float = ..., maxMemoryInMB: int = ..., cacheNodeIds: bool = ..., checkpointInterval: int = ..., impurity: str = ..., seed: Optional[int] = ..., varianceCol: Optional[str] = ..., weightCol: Optional[str] = ..., leafCol: str = ...) -> None: ...
    def setParams(self, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., maxDepth: int = ..., maxBins: int = ..., minInstancesPerNode: int = ..., minInfoGain: float = ..., maxMemoryInMB: int = ..., cacheNodeIds: bool = ..., checkpointInterval: int = ..., impurity: str = ..., seed: Optional[int] = ..., varianceCol: Optional[str] = ..., weightCol: Optional[str] = ..., leafCol: str = ...) -> DecisionTreeRegressor: ...
    def setMaxDepth(self, value: int) -> DecisionTreeRegressor: ...
    def setMaxBins(self, value: int) -> DecisionTreeRegressor: ...
    def setMinInstancesPerNode(self, value: int) -> DecisionTreeRegressor: ...
    def setMinInfoGain(self, value: float) -> DecisionTreeRegressor: ...
    def setMaxMemoryInMB(self, value: int) -> DecisionTreeRegressor: ...
    def setCacheNodeIds(self, value: bool) -> DecisionTreeRegressor: ...
    def setImpurity(self, value: str) -> DecisionTreeRegressor: ...

class DecisionTreeModel(JavaModel, JavaPredictionModel):
    @property
    def numNodes(self) -> int: ...
    @property
    def depth(self) -> int: ...
    @property
    def toDebugString(self) -> str: ...

class TreeEnsembleModel(JavaModel):
    @property
    def trees(self) -> Sequence[DecisionTreeModel]: ...
    @property
    def getNumTrees(self) -> int: ...
    @property
    def treeWeights(self) -> List[float]: ...
    @property
    def totalNumNodes(self) -> int: ...
    @property
    def toDebugString(self) -> str: ...

class DecisionTreeRegressionModel(DecisionTreeModel, JavaMLWritable, JavaMLReadable[DecisionTreeRegressionModel]):
    @property
    def featureImportances(self) -> Vector: ...

class RandomForestRegressor(JavaEstimator[RandomForestRegressionModel], HasFeaturesCol, HasLabelCol, HasPredictionCol, HasSeed, RandomForestParams, TreeRegressorParams, HasCheckpointInterval, JavaMLWritable, JavaMLReadable[RandomForestRegressor]):
    def __init__(self, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., maxDepth: int = ..., maxBins: int = ..., minInstancesPerNode: int = ..., minInfoGain: float = ..., maxMemoryInMB: int = ..., cacheNodeIds: bool = ..., checkpointInterval: int = ..., impurity: str = ..., subsamplingRate: float = ..., seed: Optional[int] = ..., numTrees: int = ..., featureSubsetStrategy: str = ...) -> None: ...
    def setParams(self, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., maxDepth: int = ..., maxBins: int = ..., minInstancesPerNode: int = ..., minInfoGain: float = ..., maxMemoryInMB: int = ..., cacheNodeIds: bool = ..., checkpointInterval: int = ..., impurity: str = ..., subsamplingRate: float = ..., seed: Optional[int] = ..., numTrees: int = ..., featureSubsetStrategy: str = ...) -> RandomForestRegressor: ...
    def setFeatureSubsetStrategy(self, value: str) -> RandomForestRegressor: ...

class RandomForestRegressionModel(TreeEnsembleModel, JavaPredictionModel, JavaMLWritable, JavaMLReadable[RandomForestRegressionModel]):
    @property
    def trees(self) -> Sequence[DecisionTreeRegressionModel]: ...
    @property
    def featureImportances(self) -> Vector: ...

class GBTRegressor(JavaEstimator[GBTRegressionModel], HasFeaturesCol, HasLabelCol, HasPredictionCol, GBTRegressorParams, HasCheckpointInterval, HasSeed, JavaMLWritable, JavaMLReadable[GBTRegressor]):
    def __init__(self, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., maxDepth: int = ..., maxBins: int = ..., minInstancesPerNode: int = ..., minInfoGain: float = ..., maxMemoryInMB: int = ..., cacheNodeIds: bool = ..., subsamplingRate: float = ..., checkpointInterval: int = ..., lossType: str = ..., maxIter: int = ..., stepSize: float = ..., seed: Optional[int] = ..., impurity: str = ..., featureSubsetStrategy: str = ..., validationTol: float = ..., validationIndicatorCol: Optional[str] = ..., leafCol: str = ...) -> None: ...
    def setParams(self, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., maxDepth: int = ..., maxBins: int = ..., minInstancesPerNode: int = ..., minInfoGain: float = ..., maxMemoryInMB: int = ..., cacheNodeIds: bool = ..., subsamplingRate: float = ..., checkpointInterval: int = ..., lossType: str = ..., maxIter: int = ..., stepSize: float = ..., seed: Optional[int] = ..., impuriy: str = ..., featureSubsetStrategy: str = ..., validationTol: float = ..., validationIndicatorCol: Optional[str] = ..., leafCol: str = ...) -> GBTRegressor: ...
    def setMaxDepth(self, value: int) -> GBTRegressor: ...
    def setMaxBins(self, value: int) -> GBTRegressor: ...
    def setMinInstancesPerNode(self, value: int) -> GBTRegressor: ...
    def setMinInfoGain(self, value: float) -> GBTRegressor: ...
    def setMaxMemoryInMB(self, value: int) -> GBTRegressor: ...
    def setCacheNodeIds(self, value: bool) -> GBTRegressor: ...
    def setImpurity(self, value: str) -> GBTRegressor: ...
    def setLossType(self, value: str) -> GBTRegressor: ...
    def setSubsamplingRate(self, value: float) -> GBTRegressor: ...
    def setFeatureSubsetStrategy(self, value: str) -> GBTRegressor: ...
    def setValidationIndicatorCol(self, value: str) -> GBTRegressor: ...

class GBTRegressionModel(TreeEnsembleModel, JavaPredictionModel, JavaMLWritable, JavaMLReadable[GBTRegressionModel]):
    @property
    def featureImportances(self) -> Vector: ...
    @property
    def trees(self) -> Sequence[DecisionTreeRegressionModel]: ...
    def evaluateEachIteration(self, dataset: DataFrame, loss: str) -> List[float]: ...

class AFTSurvivalRegression(JavaEstimator[AFTSurvivalRegressionModel], HasFeaturesCol, HasLabelCol, HasPredictionCol, HasFitIntercept, HasMaxIter, HasTol, HasAggregationDepth, JavaMLWritable, JavaMLReadable[AFTSurvivalRegression]):
    censorCol: Param
    quantileProbabilities: Param
    quantilesCol: Param
    def __init__(self, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., fitIntercept: bool = ..., maxIter: int = ..., tol: float = ..., censorCol: str = ..., quantileProbabilities: List[float] = ..., quantilesCol: Optional[str] = ..., aggregationDepth: int = ...) -> None: ...
    def setParams(self, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., fitIntercept: bool = ..., maxIter: int = ..., tol: float = ..., censorCol: str = ..., quantileProbabilities: List[float] = ..., quantilesCol: Optional[str] = ..., aggregationDepth: int = ...) -> AFTSurvivalRegression: ...
    def setCensorCol(self, value: str) -> AFTSurvivalRegression: ...
    def getCensorCol(self) -> str: ...
    def setQuantileProbabilities(self, value: List[float]) -> AFTSurvivalRegression: ...
    def getQuantileProbabilities(self) -> List[float]: ...
    def setQuantilesCol(self, value: str) -> AFTSurvivalRegression: ...
    def getQuantilesCol(self) -> str: ...

class AFTSurvivalRegressionModel(JavaModel, JavaMLWritable, JavaMLReadable[AFTSurvivalRegressionModel]):
    @property
    def coefficients(self) -> Vector: ...
    @property
    def intercept(self) -> float: ...
    @property
    def scale(self) -> float: ...
    def predictQuantiles(self, features: Vector) -> Vector: ...
    def predict(self, features: Vector) -> float: ...

class GeneralizedLinearRegression(JavaEstimator[GeneralizedLinearRegressionModel], HasLabelCol, HasFeaturesCol, HasPredictionCol, HasFitIntercept, HasMaxIter, HasTol, HasRegParam, HasWeightCol, HasSolver, JavaMLWritable, JavaMLReadable[GeneralizedLinearRegression]):
    family: Param
    link: Param
    linkPredictionCol: Param
    variancePower: Param
    linkPower: Param
    def __init__(self, labelCol: str = ..., featuresCol: str = ..., predictionCol: str = ..., family: str = ..., link: Optional[str] = ..., fitIntercept: bool = ..., maxIter: int = ..., tol: float = ..., regParam: float = ..., weightCol: Optional[str] = ..., solver: str = ..., linkPredictionCol: Optional[str] = ...,  variancePower: float = ..., linkPower: Optional[float] = ...) -> None: ...
    def setParams(self, labelCol: str = ..., featuresCol: str = ..., predictionCol: str = ..., family: str = ..., link: Optional[str] = ..., fitIntercept: bool = ..., maxIter: int = ..., tol: float = ..., regParam: float = ..., weightCol: Optional[str] = ..., solver: str = ..., linkPredictionCol: Optional[str] = ..., variancePower: float = ..., linkPower: Optional[float] = ...) -> GeneralizedLinearRegression: ...
    def setFamily(self, value: str) -> GeneralizedLinearRegression: ...
    def getFamily(self) -> str: ...
    def setLinkPredictionCol(self, value: str) -> GeneralizedLinearRegression: ...
    def getLinkPredictionCol(self) -> str: ...
    def setLink(self, value: str) -> GeneralizedLinearRegression: ...
    def getLink(self) -> str: ...
    def setVariancePower(self, value: float) -> GeneralizedLinearRegression: ...
    def getVariancePower(self) -> float: ...
    def setLinkPower(self, value: float) -> GeneralizedLinearRegression: ...
    def getLinkPower(self) -> float: ...

class GeneralizedLinearRegressionModel(JavaModel, JavaPredictionModel, JavaMLWritable, JavaMLReadable[GeneralizedLinearRegressionModel], HasTrainingSummary):
    @property
    def coefficients(self) -> Vector: ...
    @property
    def intercept(self) -> float: ...
    @property
    def summary(self) -> GeneralizedLinearRegressionTrainingSummary: ...
    @property
    def hasSummary(self) -> bool: ...
    def evaluate(self, dataset: DataFrame) -> GeneralizedLinearRegressionSummary: ...

class GeneralizedLinearRegressionSummary(JavaWrapper):
    @property
    def predictions(self) -> DataFrame: ...
    @property
    def predictionCol(self) -> str: ...
    @property
    def rank(self) -> int: ...
    @property
    def degreesOfFreedom(self) -> int: ...
    @property
    def residualDegreeOfFreedom(self) -> int: ...
    @property
    def residualDegreeOfFreedomNull(self) -> int: ...
    def residuals(self, residualsType: str = ...) -> DataFrame: ...
    @property
    def nullDeviance(self) -> float: ...
    @property
    def deviance(self) -> float: ...
    @property
    def dispersion(self) -> float: ...
    @property
    def aic(self) -> float: ...

class GeneralizedLinearRegressionTrainingSummary(GeneralizedLinearRegressionSummary):
    @property
    def numIterations(self) -> int: ...
    @property
    def solver(self) -> str: ...
    @property
    def coefficientStandardErrors(self) -> List[float]: ...
    @property
    def tValues(self) -> List[float]: ...
    @property
    def pValues(self) -> List[float]: ...
