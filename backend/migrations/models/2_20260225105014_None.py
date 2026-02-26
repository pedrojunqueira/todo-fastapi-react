from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "todo" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "text" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "completed" BOOL NOT NULL DEFAULT False
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztlm9v2jAQxr8KyisqdVXL+k97B5StTIVMNN2qVlVkEhMsHDtNLi2o6nefz4kJCRBRad"
    "Naae/gucfJ3e9sX16sUPqUJweO9KX1pfFiCRJS9aOk7zcsEkWFigKQMddGMI5xAjHxQGkT"
    "whOqJJ8mXswiYFIoVaScoyg9ZWQiKKRUsMeUuiADClMaq8D9g5KZ8OmcJuZvNHMnjHK/lC"
    "bz8d1ad2ERaa0v4Ks24tvGrid5GorCHC1gKsXSzQSgGlBBYwIUHw9xiuljdnmVpqIs08KS"
    "pbiyxqcTknJYKXdHBp4UyE9lk+gCA3zLp9bR8dnx+efT43Nl0ZkslbPXrLyi9myhJjB0rF"
    "cdJ0Ayh8ZYcAM6h3VyjlI3ozP+CjyVchWeQVVHzwgFvmLL/Bl+NXCc3q2DSYdJ8shRGP5s"
    "j7qX7VFz0L7d05FFHrmyh9+MXarNne34YffK7mi+BU8vpli/SzZQvVARYCHdTLa8ssLXz5"
    "cemB/vk7alavBtwRf5Qaij3x/0rp324EepBRdtp4eRVgm/UZune+UOLB/S+NV3Lhv4t3Fn"
    "D3uaoEwgiPUbC59zZ2FOJAXpCvnsEn/lzBrVgCk3VoYRpwh7ra8dKTklYktbV9dVujpWC/"
    "9WI9969+5+bjq2fVVqWqdfPRg3g05v1DzS3VImBrS4jfAKn8xWLiMUxsSbPZPYd9cisiW3"
    "eddDYSusKkSQQCPCOrGqfKC1acy86aZRl0dqhx0pPP/H3Qcad080TjClNXjdKYk301tZ8l"
    "GGntr1c5dTEQBu8NbJSQ0zM/OUq3K5mnHYymLlOYdH4w0Qc/vHBHh0eLgDQOXaClDHKh8K"
    "UgAVG74Svl/bw22jZLmkAvJGqALvfebBfoOzBB7eJ9Yailh1/cdY9burMuLxAZ1/PV5efw"
    "Ovkzo8"
)
