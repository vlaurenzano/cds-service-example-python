import cds_hooks_work as cds
import os

app = cds.App()


@app.patient_view("patient-greeting", "The patient greeting service greets a patient!", title="Patient Greeter")
def greeting(r: cds.PatientViewRequest) -> cds.Response:
    resp = cds.Response()
    resp.cards = [cds.Card.info("hello world!", "demo_service")]
    return resp


if __name__ == '__main__':
    debug = os.environ.get('DEBUG', False)
    port = os.environ.get("PORT", 5000)
    app.serv(host="0.0.0.0", debug=debug, port=port)
