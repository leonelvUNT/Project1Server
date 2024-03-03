from flask import Flask, jsonify, request
import python_jwt as jwt, jwcrypto.jwk as jwk, datetime

app = Flask(__name__)

daJWKSList = {}

"""
key = jwk.JWK.generate(kty='RSA', size=2048)

payload = {
    'iss':'ISSUER', 
    'sub':'SUBJECT', 
    'aud':'AUDIENCE', 
    'role': 'user', 
    'permission': 'read' 
}


private_key = key.export_private()
public_key = key.export_public()

token = jwt.generate_jwt(payload, jwk.JWK.from_json(private_key), 'RS256', datetime.timedelta(minutes=50))
"""
# ______________________________ Step 4 ______________________________________
# ______________________________ VALIDATE JWT TOKEN USING PUBLIC KEY ______________________________________


# To validate JWT Token, you need the public key as a JWK object
#header, claims = jwt.verify_jwt(token, jwk.JWK.from_json(public_key), ['RS256'])

@app.route("/.well-known/jwks.json", methods=["GET"])
def getJWKS():
    """
    Returns a JWKS of all JWKs on the server
    """
    # do stuff
    return daJWKSList, 200

@app.route("/auth", methods=["POST"])
def createJWT():
    """
    Create a JWK and return a corresponding JWT
    """
    # do stuff here too
    extra = request.args.get("extra")
    if extra:
        """
        Check and send Expired JWT 
        """
        return expiredJWT, 200
    else:
        
        key = jwk.JWK.generate(kty='RSA', size=2048)

        payload = {
            'iss':'ISSUER', 
            'sub':'SUBJECT', 
            'aud':'AUDIENCE', 
            'role': 'user', 
            'permission': 'read' 
        }


        private_key = key.export_private()
        public_key = key.export_public()

        token = jwt.generate_jwt(payload, jwk.JWK.from_json(private_key), 'RS256', datetime.timedelta(minutes=50))



        return token, 200





if __name__ == "__main__":
    app.run(port=8080)