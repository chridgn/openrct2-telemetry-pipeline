from pydantic import BaseModel
from typing import List, Optional

class Metrics(BaseModel):
    averageCash: float
    averageHappiness: float
    parkRating: int
    rideReliability: float
    averageQueueTime: float
    averageRideDowntime: float
    averageRideSatisfaction: float


class GuestSegmentation(BaseModel):
    total: int
    happy: int
    neutral: int
    unhappy: int
    nauseated: int
    hungry: int
    thirsty: int
    lost: int
    broke: int
    totalSpendingPower: float


class Revenue(BaseModel):
    totalIncomeFromAdmissions: float
    entranceFee: float
    totalAdmissions: int
    cash: float
    bankLoan: float
    companyValue: float
    parkValue: float


class Ride(BaseModel):
    id: int
    name: str
    type: int
    status: str
    totalCustomers: int
    totalProfit: float
    runningCost: float
    buildCost: float
    excitement: float
    intensity: float
    nausea: float
    reliability: float
    downtime: float
    satisfaction: float
    age: int
    avgQueueTime: float


class Staff(BaseModel):
    handymenCount: int
    mechanicCount: int
    securityCount: int
    entertainerCount: int
    ridesPerMechanic: Optional[float] = None  # null when no mechanics present


class ParkIdentity(BaseModel):
    name: str
    scenarioFilename: str


class Environment(BaseModel):
    weather: str
    temperature: float
    month: int
    year: int


class Snapshot(BaseModel):
    tick: int
    type: str
    park: ParkIdentity
    environment: Environment
    metrics: Metrics
    guests: GuestSegmentation
    revenue: Revenue
    rides: List[Ride]
    staff: Staff

