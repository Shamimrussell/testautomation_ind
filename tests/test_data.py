from faker import Faker

fake = Faker("sv_SE")

print(fake.name())
print(fake.email())
print(fake.address())