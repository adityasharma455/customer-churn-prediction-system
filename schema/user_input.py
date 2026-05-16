from pydantic import BaseModel, Field
from typing import Literal, Annotated

# ✅ Input Schema using Annotated
class CustomerInput(BaseModel):

    gender: Annotated[Literal["Male", "Female"], Field(description="Customer gender")]

    SeniorCitizen: Annotated[int, Field(ge=0, le=1, description="0 = No, 1 = Yes")]

    Partner: Annotated[Literal["Yes", "No"], Field(description="Has partner or not")]
    Dependents: Annotated[Literal["Yes", "No"], Field(description="Has dependents or not")]

    tenure: Annotated[int, Field(ge=0, description="Number of months customer stayed")]

    PhoneService: Annotated[Literal["Yes", "No"], Field()]
    MultipleLines: Annotated[Literal["Yes", "No", "No phone service"], Field()]

    InternetService: Annotated[Literal["DSL", "Fiber optic", "No"], Field()]

    OnlineSecurity: Annotated[Literal["Yes", "No", "No internet service"], Field()]
    OnlineBackup: Annotated[Literal["Yes", "No", "No internet service"], Field()]
    DeviceProtection: Annotated[Literal["Yes", "No", "No internet service"], Field()]
    TechSupport: Annotated[Literal["Yes", "No", "No internet service"], Field()]

    StreamingTV: Annotated[Literal["Yes", "No", "No internet service"], Field()]
    StreamingMovies: Annotated[Literal["Yes", "No", "No internet service"], Field()]

    Contract: Annotated[
        Literal["Month-to-month", "One year", "Two year"],
        Field(description="Contract type")
    ]

    PaperlessBilling: Annotated[Literal["Yes", "No"], Field()]

    PaymentMethod: Annotated[
        Literal[
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ],
        Field(description="Payment method used")
    ]

    MonthlyCharges: Annotated[float, Field(gt=0, description="Monthly bill amount")]

    TotalCharges: Annotated[float, Field(ge=0, description="Total amount charged")]
