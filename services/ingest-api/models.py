from pydantic import BaseModel
from typing import List, Optional

class Metrics(BaseModel):
    averageCash: Optional[float] = None
    averageHappiness: Optional[float] = None
    parkRating: Optional[int] = None
    rideReliability: Optional[float] = None
    averageQueueTime: Optional[float] = None
    averageRideDowntime: Optional[float] = None
    averageRideSatisfaction: Optional[float] = None


class GuestSegmentation(BaseModel):
    total: Optional[int] = None
    happy: Optional[int] = None
    neutral: Optional[int] = None
    unhappy: Optional[int] = None
    nauseated: Optional[int] = None
    hungry: Optional[int] = None
    thirsty: Optional[int] = None
    lost: Optional[int] = None
    broke: Optional[int] = None
    totalSpendingPower: Optional[float] = None


class Revenue(BaseModel):
    totalIncomeFromAdmissions: Optional[float] = None
    entranceFee: Optional[float] = None
    totalAdmissions: Optional[int] = None
    cash: Optional[float] = None
    bankLoan: Optional[float] = None
    companyValue: Optional[float] = None
    parkValue: Optional[float] = None


class Ride(BaseModel):
    id: int
    name: str
    type: int
    status: str
    totalCustomers: Optional[int] = None
    totalProfit: Optional[float] = None
    runningCost: Optional[float] = None
    buildCost: Optional[float] = None
    excitement: Optional[float] = None
    intensity: Optional[float] = None
    nausea: Optional[float] = None
    reliability: Optional[float] = None
    downtime: Optional[float] = None
    satisfaction: Optional[float] = None
    age: Optional[int] = None
    avgQueueTime: Optional[float] = None


class Staff(BaseModel):
    handymenCount: Optional[int] = None
    mechanicCount: Optional[int] = None
    securityCount: Optional[int] = None
    entertainerCount: Optional[int] = None
    ridesPerMechanic: Optional[float] = None  # null when no mechanics present


class ParkIdentity(BaseModel):
    name: str
    scenarioFilename: str


class Environment(BaseModel):
    weather: Optional[str] = None
    temperature: Optional[float] = None
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
