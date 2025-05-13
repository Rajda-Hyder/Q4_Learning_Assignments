from pydantic import BaseModel, EmailStr, field_validator, ValidationError
from typing import List

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class UserWithAddress(BaseModel):
    id: int
    name: str
    email: EmailStr
    addresses: List[Address]

# we use Pydantic V1 style `@validator` validators are deprecated.so migrate to Pydantic V2 style `@field_validator`

    @field_validator("name")
    @classmethod
    def name_must_be_at_least_two_chars(cls, v):
        if len(v) < 2:
            raise ValueError("Name must be at least 2 characters long")
        return v

# Test with invalid data
try:
    invalid_user = UserWithAddress(
        id=3,
        name="A",  # Too short
        email="charlie@example.com",
        addresses=[{"street": "789 Pine Rd", "city": "Chicago", "zip_code": "60601"}],
    )
except ValidationError as e:
    
    print("\n" + "="*50 + "\n")
    print("Validation failed:")
    print(e)
    print("\n" + "="*50 + "\n")

# ✅ Test with valid data
try:
    valid_user = UserWithAddress(
        id=1,
        name="Alice",
        email="alice@example.com",
        addresses=[
            {"street": "123 Main St", "city": "New York", "zip_code": "10001"},
            {"street": "456 Oak Ave", "city": "Los Angeles", "zip_code": "90001"},
        ],
    )
    print("Valid user created successfully:")
    print(valid_user)
    print("As dictionary:", valid_user.model_dump())  # Optional
except ValidationError as e:
    print("Validation failed:")
    print(e)
