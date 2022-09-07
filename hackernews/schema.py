import graphene
import graphql_jwt
import links.schema
from hackernews.users import schema 
import links.schema_relay

class Query(
    schema.Query,
    links.schema.Query,
    links.schema_relay.RelayQuery,
    graphene.ObjectType,
    ):
    pass

class Mutation(schema.Mutation,
            links.schema.Mutation,
            links.schema_relay.RelayMutation,
            graphene.ObjectType):
            
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()




schema = graphene.Schema(query=Query, mutation=Mutation)